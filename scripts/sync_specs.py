#!/usr/bin/env python3
"""Keep the MCP packages in sync with the official Atlassian OpenAPI documents.

For every package in scripts/specs.json this script downloads the official spec, compares it with the
package database (packages/<id>/mcp.db) and reports what changed:

  * added    - operations in the spec that have no request/tool yet (a new row is generated, following the
               conventions already used by the package; deprecated operations are skipped)
  * removed  - requests whose operation no longer exists in the spec (deleted only with --prune)
  * changed  - existing operations whose path/query parameters changed (rows regenerated in place)
  * deprecated - existing operations the spec now marks as deprecated (reported only)

Modes:
  --check   report only, write nothing (exit 10 when something differs, 0 when in sync)
  --apply   write the databases, the index notes and the manifests (exit 10 when operations changed)

Standard library only, so it runs unchanged in GitHub Actions.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import sqlite3
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKAGES = ROOT / "packages"
CONFIG = Path(__file__).resolve().parent / "specs.json"
METHODS = ("get", "post", "put", "patch", "delete")
EXIT_CHANGED = 10

# ---------------------------------------------------------------------------------------------------------
# Spec helpers
# ---------------------------------------------------------------------------------------------------------


def norm_path(path: str) -> str:
    """Path with every whole-segment placeholder ({id}, {issueIdOrKey}...) reduced to {} so names can differ."""
    segments = ["{}" if re.fullmatch(r"\{[^}/]*\}", seg) else seg for seg in path.split("/")]
    return "/".join(segments).rstrip("/") or "/"


HEADER_CONSTANTS = {"x-atlassian-token": "no-check"}


def header_param(name: str) -> str:
    return snake(name).lower()


def snake(name: str) -> str:
    """Parameter name as the tools spell it: any character that is not a letter, digit or _ becomes _."""
    return re.sub(r"[^A-Za-z0-9_]", "_", name)


def deref(spec: dict, obj, depth: int = 0):
    while isinstance(obj, dict) and "$ref" in obj and depth < 12:
        node = spec
        for part in obj["$ref"].lstrip("#/").split("/"):
            node = node.get(part, {}) if isinstance(node, dict) else {}
        obj = node
        depth += 1
    return obj


def clean_inline(text: str | None, limit: int | None = None) -> str:
    """Single-line plain text: markdown links reduced to their label, whitespace collapsed."""
    text = text or ""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[*`]{1,3}", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        cut = text[:limit]
        text = cut[: cut.rfind(" ")] if " " in cut else cut
        text = text.rstrip(".,;:") + "..."
    return text


def make_example(spec: dict, schema, depth: int = 0, seen: tuple = ()):
    schema = deref(spec, schema)
    if not isinstance(schema, dict) or depth > 4:
        return None
    if "example" in schema:
        return schema["example"]
    if "default" in schema and not isinstance(schema["default"], (dict, list)):
        return schema["default"]
    for key in ("allOf",):
        if key in schema:
            merged: dict = {}
            for sub in schema[key]:
                ex = make_example(spec, sub, depth + 1, seen)
                if isinstance(ex, dict):
                    merged.update(ex)
            return merged or None
    for key in ("oneOf", "anyOf"):
        if schema.get(key):
            return make_example(spec, schema[key][0], depth + 1, seen)
    if "enum" in schema and schema["enum"]:
        return schema["enum"][0]
    kind = schema.get("type")
    if kind == "object" or "properties" in schema:
        ref = id(schema)
        if ref in seen:
            return {}
        out = {}
        for i, (name, sub) in enumerate((schema.get("properties") or {}).items()):
            if i >= 14:
                break
            out[name] = make_example(spec, sub, depth + 1, seen + (ref,))
        return out
    if kind == "array":
        item = make_example(spec, schema.get("items", {}), depth + 1, seen)
        return [item] if item is not None else []
    if kind == "integer" or kind == "number":
        return 0
    if kind == "boolean":
        return False
    if kind == "string":
        fmt = schema.get("format")
        return {"date-time": "2026-01-01T00:00:00.000Z", "date": "2026-01-01", "uri": "https://example.com"}.get(fmt, "string")
    return None


class Op:
    """One operation of a spec, normalised across OpenAPI 3 and Swagger 2."""

    def __init__(self, spec: dict, path: str, method: str, item: dict, op: dict):
        self.path = path
        self.method = method.upper()
        self.op = op
        self.summary = clean_inline(op.get("summary")) or clean_inline(op.get("operationId")) or f"{self.method} {path}"
        self.description = (op.get("description") or "").strip()
        tags = op.get("tags") or []
        self.category = tags[0] if tags else "General"
        self.deprecated = bool(op.get("deprecated"))
        head = (self.summary + " " + self.description[:300]).upper()
        self.experimental = bool(op.get("x-experimental")) or "EXPERIMENTAL" in head
        # Parameters: path-item level first, operation level overrides.
        merged: dict = {}
        for raw in list(item.get("parameters", [])) + list(op.get("parameters", [])):
            prm = deref(spec, raw)
            if isinstance(prm, dict) and prm.get("name"):
                merged[(prm.get("in"), prm["name"])] = prm
        # Some specs forget to declare a path placeholder as a parameter: add it so the tool still asks for it.
        for name in re.findall(r"\{([^}]+)\}", path):
            if ("path", name) not in merged:
                merged[("path", name)] = {"in": "path", "name": name, "required": True}
        self.params = [p for p in merged.values() if p.get("in") in ("path", "query", "header")]
        self.body_required = False
        self.body_type: str | None = None
        self.body_example = None
        self._read_body(spec, op, merged)
        if not self.body_type and self.method in ("POST", "PUT", "PATCH") and re.search(r"request body|application/json", self.description, re.I):
            # Some specs describe the body only in prose; still let the caller send one.
            self.body_type = "application/json"
        self.accepts_json = self._accepts_json(spec, op)

    def _read_body(self, spec: dict, op: dict, merged: dict) -> None:
        body = deref(spec, op.get("requestBody"))
        if isinstance(body, dict) and body.get("content"):
            content = body["content"]
            ctype = "application/json" if "application/json" in content else next(iter(content))
            media = content[ctype]
            self.body_type = ctype
            self.body_required = bool(body.get("required"))
            ex = media.get("example")
            if ex is None and isinstance(media.get("examples"), dict) and media["examples"]:
                first = deref(spec, next(iter(media["examples"].values())))
                ex = first.get("value") if isinstance(first, dict) else None
            if ex is None and media.get("schema") is not None:
                ex = make_example(spec, media["schema"])
            self.body_example = ex
            return
        for (where, _name), prm in merged.items():  # Swagger 2
            if where == "body":
                self.body_type = "application/json"
                self.body_required = bool(prm.get("required"))
                self.body_example = make_example(spec, prm.get("schema", {}))
                return
            if where == "formData":
                self.body_type = "multipart/form-data"

    @staticmethod
    def _accepts_json(spec: dict, op: dict) -> bool:
        for code, resp in (op.get("responses") or {}).items():
            if not str(code).startswith("2"):
                continue
            resp = deref(spec, resp)
            if isinstance(resp, dict) and any("json" in c for c in (resp.get("content") or {})):
                return True
            if isinstance(resp, dict) and resp.get("schema") and "json" in " ".join(op.get("produces", ["application/json"])):
                return True
        return False

    def signature(self) -> str:
        parts = sorted(f"{p['in']}:{p['name']}:{int(bool(p.get('required')))}" for p in self.params)
        return json.dumps([self.method, norm_path(self.path), self.summary, self.deprecated, parts, self.body_type])


def load_ops(spec: dict) -> dict[tuple[str, str], Op]:
    ops: dict[tuple[str, str], Op] = {}
    for path, item in (spec.get("paths") or {}).items():
        for method in METHODS:
            if isinstance(item.get(method), dict):
                ops[(method.upper(), norm_path(path))] = Op(spec, path, method, item, item[method])
    return ops


# ---------------------------------------------------------------------------------------------------------
# Row generation (mirrors the layout of the existing request notes and tools)
# ---------------------------------------------------------------------------------------------------------

VERB_LIST = ("get", "list", "search", "find", "check", "validate", "count", "retrieve", "query", "export", "evaluate")


def operation_kind(op: Op) -> str:
    low = op.summary.lower()
    if op.method == "GET":
        return "list" if not op.path.rstrip("/").endswith("}") else "get"
    if op.method == "DELETE":
        return "delete"
    if op.method in ("PUT", "PATCH"):
        return "update"
    return "list" if low.startswith(VERB_LIST) else "create"


def kebab(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "general"


def snake_id(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


class PackageContext:
    """Per-package conventions read from the existing rows plus specs.json."""

    def __init__(self, pkg_id: str, cfg: dict, con: sqlite3.Connection):
        self.id = pkg_id
        self.cfg = cfg
        self.title_prefix = cfg["title_prefix"]
        self.tool_prefix = cfg.get("tool_prefix")
        self.base = cfg["base"]
        self.service_params = cfg.get("service_params", {})
        self.request_only_prefixes = cfg.get("request_only_prefixes", [])
        self.runner = cfg.get("request_runner", "atlassian_request")
        row = con.execute("select doc_url, tags from requests where doc_url is not null limit 1").fetchone()
        self.doc_url = row[0] if row else ""
        tags = json.loads(row[1]) if row and row[1] else []
        self.static_tags = [t for t in tags if t.startswith(("api/service/", "api/app/"))]
        self.version_tags = [t for t in tags if t.startswith("api/version/")]
        trow = con.execute("select service_tag, service_param, service_exclude_tag, tags from tools limit 1").fetchone()
        self.has_tools = trow is not None or bool(self.tool_prefix and con.execute("select count(*) from tools").fetchone()[0])
        self.tool_service = trow[:3] if trow else (None, None, None)
        if trow and trow[3]:
            ttags = json.loads(trow[3])
            self.static_tags = [t for t in ttags if t.startswith(("api/service/", "api/app/"))] or self.static_tags
            self.version_tags = [t for t in ttags if t.startswith("api/version/")] or self.version_tags
        self.titles = {r[0] for r in con.execute("select id from requests")}
        self.tool_ids = {r[0] for r in con.execute("select id from tools")}

    def url_for(self, op: Op) -> str:
        def sub(match: re.Match) -> str:
            name = match.group(1)
            if name in self.service_params:
                return "{{service." + self.service_params[name] + "}}"
            return "{{param:" + snake(name) + "}}"

        url = self.base + re.sub(r"\{([^}]*)\}", sub, op.path)
        queries = [p for p in op.params if p["in"] == "query"]
        if queries:
            url += "?" + "&".join(f"{p['name']}={{{{param:{snake(p['name'])}}}}}" for p in queries)
        return url

    def visible_params(self, op: Op) -> list[dict]:
        # Placeholders in the package base URL (e.g. Automation's {{param:product}}) are parameters too.
        out = [{"in": "path", "name": name, "required": True} for name in re.findall(r"\{\{param:(\w+)\}\}", self.base)]
        for p in op.params:
            if p["in"] == "path" and p["name"] in self.service_params:
                continue
            if p["in"] == "header" and p["name"].lower() in ("authorization", "accept", "content-type", *HEADER_CONSTANTS):
                continue
            out.append(p)
        return out

    def request_only(self, op: Op) -> bool:
        if not self.has_tools:
            return True
        if any(op.path.startswith(prefix) for prefix in self.request_only_prefixes):
            return True
        return bool(op.body_type and "json" not in op.body_type and "form-urlencoded" not in op.body_type)

    def unique(self, base: str, taken: set[str], suffix: str) -> str:
        if base not in taken:
            return base
        alt = f"{base} ({suffix})"
        return alt if alt not in taken else f"{alt} {len(taken)}"

    def build(self, op: Op, title: str | None = None, tool_id: str | None = None, force_request_only: bool | None = None):
        """Returns (request_row, tool_row | None)."""
        title = title or self.unique(f"{self.title_prefix} - {op.summary}", self.titles, op.method)
        only = self.request_only(op) if force_request_only is None else force_request_only
        writes = op.method != "GET"
        sends_body = bool(op.body_type and ("json" in op.body_type or "form-urlencoded" in op.body_type))
        visible = self.visible_params(op)
        tool_name = None
        if not only:
            tool_name = tool_id or self.unique_tool_id(op)
        lines = [f"# {title}", "", f"**{op.summary}** — `{op.method} {op.path}`", ""]
        if tool_name:
            lines.append(f"- Run by the tool [[{tool_name}]].")
        else:
            verb = "write" if writes else "read"
            lines.append(f'- No dedicated tool: run it with `{self.runner}_{verb}` passing `request:"{title}"`.')
        if op.experimental:
            lines.append("- **Stability:** experimental; the API may change without notice.")
        if op.body_type and "json" not in op.body_type and "form-urlencoded" not in op.body_type:
            lines.append("- **Restriction:** multipart/binary body; not supported by the generic request runner.")
        elif any(op.path.startswith(prefix) for prefix in self.request_only_prefixes):
            lines.append("- **Restriction:** requires app OAuth 2.0 / JWT credentials, not the user Basic token.")
        lines.append(f"- Official documentation: {self.doc_url}")
        lines += ["", "```http", f"{op.method} {self.url_for(op)}", "Authorization: {{service.auth_token}}"]
        if op.method == "GET" or (op.accepts_json and not sends_body):
            lines.append("Accept: application/json")
        for name, value in HEADER_CONSTANTS.items():
            if any(p["in"] == "header" and p["name"].lower() == name for p in op.params):
                lines.append(f"X-Atlassian-Token: {value}")
        for p in visible:
            if p["in"] == "header":
                lines.append(f"{p['name']}: {{{{param:{header_param(p['name'])}}}}}")
        if sends_body:
            lines.append(f"Content-Type: {op.body_type}")
            lines += ["", "{{param:body}}"]
        lines.append("```")
        if visible or sends_body:
            lines += ["", "## Parameters", ""]
        schema: dict = {}
        for p in visible:
            name = header_param(p["name"]) if p["in"] == "header" else snake(p["name"])
            desc = clean_inline(p.get("description")) or f"Value of {p['name']} in the {p['in']}."
            req = bool(p.get("required")) or p["in"] == "path"
            lines.append(f"- `{name}` ({p['in']}, string, {'required' if req else 'optional'}) — {desc}")
            schema[name] = {"type": "string", "required": req, "description": desc}
        if sends_body:
            bdesc = "JSON request body. See the example in the request note."
            lines.append(f"- `body` (body, object, required) — {bdesc}")
            schema["body"] = {"type": "object", "required": True, "description": bdesc}
        if sends_body and op.body_example is not None:
            text = json.dumps(op.body_example, indent=2, ensure_ascii=False)
            if len(text) <= 4000:
                lines += ["", "## Body (example)", "", "```json", text, "```"]
        if op.description:
            lines += ["", "## Original description", "", op.description]
        resource = f"api/resource/{kebab(op.category)}"
        kind = f"api/operation/{operation_kind(op)}"
        effect = "api/effect/write" if writes else "api/effect/read"
        extra = ["api/stability/experimental"] if op.experimental else []
        req_tags = ["api/request"] + self.static_tags[:1] + self.static_tags[1:] + [resource, kind, effect] + extra + self.version_tags
        request_row = (title, title, op.method, op.path, op.category, 1 if writes else 0, self.doc_url,
                       "\n".join(lines).rstrip() + "\n", None, None, json.dumps(req_tags))
        tool_row = None
        if tool_name:
            tool_tags = ["mcp/tool"] + self.static_tags + [resource, kind, effect] + extra + self.version_tags
            desc = f"{self.title_prefix} — {op.method} {op.path} — {op.summary}."
            body = clean_inline(op.description, 320)
            if body:
                desc += " " + body
            if writes:
                desc += " Writes data: yes."
            tool_row = (tool_name, title, "request", title, desc, self.tool_service[0], self.tool_service[1],
                        self.tool_service[2], json.dumps(schema), json.dumps(tool_tags))
        return request_row, tool_row

    def unique_tool_id(self, op: Op) -> str:
        base = f"{self.tool_prefix}_{snake_id(op.summary)}"
        for candidate in (base, f"{base}_{op.method.lower()}", f"{base}_{op.method.lower()}_{len(self.tool_ids)}"):
            if candidate not in self.tool_ids:
                self.tool_ids.add(candidate)
                return candidate
        return base


# ---------------------------------------------------------------------------------------------------------
# Database, index note and manifest updates
# ---------------------------------------------------------------------------------------------------------

PARAM_LINE = re.compile(r"^- `([^`]+)` \((path|query|header|body),", re.M)


def stored_params(description: str) -> set[tuple[str, str]]:
    return {(loc, name) for name, loc in PARAM_LINE.findall(description or "") if loc in ("path", "query")}


def spec_params(ctx: PackageContext, op: Op) -> set[tuple[str, str]]:
    return {(p["in"], snake(p["name"])) for p in ctx.visible_params(op) if p["in"] in ("path", "query")}


def ensure_columns(con: sqlite3.Connection) -> None:
    have = {r[1] for r in con.execute("pragma table_info(mcp_package)")}
    for column in ("spec_url", "spec_version", "spec_fingerprint", "synced_at"):
        if column not in have:
            con.execute(f"alter table mcp_package add column {column} TEXT")


def bump(version: str) -> str:
    m = re.match(r"^(\d+)\.(\d+)\.(\d+)$", version or "")
    return f"{m.group(1)}.{int(m.group(2)) + 1}.0" if m else "1.1.0"


def update_index(pkg_dir: Path, added, removed, tools: int, only: int) -> bool:
    """Edit the package index note in place: new bullets, deleted bullets and the two counters."""
    notes = list(pkg_dir.glob("MCP - *.md"))
    if not notes:
        return False
    path = notes[0]
    lines = path.read_text(encoding="utf-8").split("\n")
    for method, route in removed:
        needle = f"`{method} {route}`"
        lines = [ln for ln in lines if not (ln.startswith("- ") and needle in ln)]
    for category, bullet in added:
        header = f"## {category}"
        if header in lines:
            idx = lines.index(header) + 1
            end = idx
            while end < len(lines) and not lines[end].startswith("## "):
                end += 1
            while end > idx and not lines[end - 1].strip():
                end -= 1
            lines.insert(end, bullet)
        else:
            if lines and lines[-1].strip():
                lines.append("")
            lines += [header, "", bullet]
    text = "\n".join(lines)
    text = re.sub(r"(\*\*Tools:\*\* )\d+", rf"\g<1>{tools}", text, count=1)
    text = re.sub(r"(\*\*Requests only:\*\* )\d+", rf"\g<1>{only}", text, count=1)
    path.write_text(text, encoding="utf-8")
    return True


def index_bullet(tool_id: str | None, title: str, op: Op, restricted: bool) -> str:
    head = f"`{tool_id}`" if tool_id else f"**{title}**"
    tail = (" ✏️" if op.method != "GET" else "") + (" \U0001f512" if restricted else "")
    return f"- {head} — `{op.method} {op.path}` — {op.summary}{tail}"


def fetch_spec(cfg: dict, spec_dir: Path | None, pkg_id: str) -> tuple[bytes, dict]:
    if spec_dir:
        raw = (spec_dir / f"{pkg_id}.json").read_bytes()
    else:
        req = urllib.request.Request(cfg["spec_url"], headers={"User-Agent": "environment-keys-mcp-packages-sync"})
        with urllib.request.urlopen(req, timeout=120) as resp:  # noqa: S310 - fixed https URLs from specs.json
            raw = resp.read()
    return raw, json.loads(raw)


def sync_package(pkg_id: str, cfg: dict, args, report: list[str]) -> dict:
    db_path = PACKAGES / pkg_id / "mcp.db"
    result = {"id": pkg_id, "added": 0, "removed": 0, "changed": 0, "deprecated": 0, "skipped": None}
    if not cfg.get("spec_url") or not db_path.exists():
        result["skipped"] = cfg.get("note") or "no spec_url"
        return result
    raw, spec = fetch_spec(cfg, Path(args.spec_dir) if args.spec_dir else None, pkg_id)
    ops = load_ops(spec)
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    ensure_columns(con)
    ctx = PackageContext(pkg_id, cfg, con)
    tools_by_request = {r["request_id"]: r["id"] for r in con.execute("select id, request_id from tools")}
    existing = {}
    for row in con.execute("select id, method, path, description from requests"):
        existing[(row["method"].upper(), norm_path(row["path"]))] = row
    added_ops = [o for k, o in ops.items() if k not in existing and not o.deprecated]
    removed_keys = [k for k in existing if k not in ops]
    changed, deprecated = [], []
    for key, row in existing.items():
        op = ops.get(key)
        if not op:
            continue
        if op.deprecated:
            deprecated.append(op)
        if stored_params(row["description"]) != spec_params(ctx, op):
            changed.append((row, op))
    fingerprint = hashlib.sha256("\n".join(sorted(o.signature() for o in ops.values())).encode()).hexdigest()
    old = con.execute("select spec_fingerprint, version from mcp_package limit 1").fetchone()
    first_baseline = old is None or old["spec_fingerprint"] is None
    result.update(added=len(added_ops), removed=len(removed_keys), changed=len(changed), deprecated=len(deprecated))

    report.append(f"### {pkg_id} — spec {spec.get('info', {}).get('version', '?')}")
    for op in sorted(added_ops, key=lambda o: (o.path, o.method)):
        report.append(f"- added: `{op.method} {op.path}` — {op.summary}" + (" (experimental)" if op.experimental else ""))
    for key in removed_keys:
        report.append(f"- removed from spec: `{existing[key]['method']} {existing[key]['path']}` ({existing[key]['id']})")
    for row, op in changed:
        report.append(f"- parameters changed: `{op.method} {op.path}` ({row['id']})")
    for op in deprecated:
        report.append(f"- now deprecated: `{op.method} {op.path}`")
    if not (added_ops or removed_keys or changed or deprecated):
        report.append("- in sync")
    report.append("")

    ops_changed = bool(added_ops or (removed_keys and args.prune) or changed)
    if args.mode == "apply" and (ops_changed or first_baseline or (old and old["spec_fingerprint"] != fingerprint)):
        index_added, index_removed = [], []
        if removed_keys and args.prune:
            for key in removed_keys:
                rid = existing[key]["id"]
                for (gone_tool,) in con.execute("select id from tools where request_id = ?", (rid,)).fetchall():
                    ctx.tool_ids.discard(gone_tool)
                con.execute("delete from tools where request_id = ?", (rid,))
                con.execute("delete from requests where id = ?", (rid,))
                ctx.titles.discard(rid)
                index_removed.append((existing[key]["method"].upper(), existing[key]["path"]))
        for row, op in changed:
            rid = row["id"]
            req_row, tool_row = ctx.build(op, title=rid, tool_id=tools_by_request.get(rid), force_request_only=rid not in tools_by_request)
            con.execute("update requests set description = ?, tags = ?, category = ? where id = ?", (req_row[7], req_row[10], req_row[4], rid))
            if tool_row:
                con.execute("update tools set params_schema = ?, description = ? where id = ?", (tool_row[8], tool_row[4], tool_row[0]))
        for op in added_ops:
            req_row, tool_row = ctx.build(op)
            ctx.titles.add(req_row[0])
            con.execute("insert into requests values (?,?,?,?,?,?,?,?,?,?,?)", req_row)
            if tool_row:
                con.execute("insert into tools (id,title,kind,request_id,description,service_tag,service_param,service_exclude_tag,params_schema,tags) values (?,?,?,?,?,?,?,?,?,?)", tool_row)
            restricted = "**Restriction:**" in req_row[7]
            index_added.append((op.category, index_bullet(tool_row[0] if tool_row else None, req_row[0], op, restricted)))
        con.execute("insert into tools_fts(tools_fts) values('rebuild')")
        tools = con.execute("select count(*) from tools").fetchone()[0]
        total = con.execute("select count(*) from requests").fetchone()[0]
        only = con.execute("select count(*) from requests where id not in (select request_id from tools where request_id is not null)").fetchone()[0]
        now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        version = bump(old["version"]) if ops_changed and old else (old["version"] if old else "1.0.0")
        sets = "tool_count = ?, request_count = ?, version = ?, spec_url = ?, spec_version = ?, spec_fingerprint = ?, synced_at = ?"
        values = [tools, total, version, cfg["spec_url"], str(spec.get("info", {}).get("version", "")), fingerprint, now]
        if ops_changed:
            sets += ", updated_at = ?"
            values.append(now)
        con.execute(f"update mcp_package set {sets}", values)
        con.commit()
        if ops_changed:
            con.execute("vacuum")
            update_index(PACKAGES / pkg_id, index_added, index_removed, tools, only)
        update_manifests(pkg_id, tools, total, only, version, str(spec.get("info", {}).get("version", "")), now)
    con.close()
    return result


def update_manifests(pkg_id: str, tools: int, total: int, only: int, version: str, spec_version: str, now: str) -> None:
    local = PACKAGES / pkg_id / "manifest.json"
    if local.exists():
        data = json.loads(local.read_text(encoding="utf-8"))
        data.update(toolCount=tools, requestCount=total)
        local.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    root = ROOT / "manifest.json"
    data = json.loads(root.read_text(encoding="utf-8"))
    for entry in data.get("packages", []):
        if entry.get("id") == pkg_id:
            entry.update(toolCount=tools, requestOnlyCount=only, requestCount=total, version=version, specVersion=spec_version, updatedAt=now)
    root.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", dest="mode", action="store_const", const="check")
    mode.add_argument("--apply", dest="mode", action="store_const", const="apply")
    parser.add_argument("--only", action="append", help="package id (repeatable); default: all")
    parser.add_argument("--prune", action="store_true", help="delete requests/tools whose operation left the spec")
    parser.add_argument("--spec-dir", help="read <package-id>.json from this folder instead of downloading (tests)")
    parser.add_argument("--report", help="write the markdown report to this file")
    args = parser.parse_args()

    config = json.loads(CONFIG.read_text(encoding="utf-8"))["packages"]
    report: list[str] = [f"# MCP package sync ({args.mode})", ""]
    totals = {"added": 0, "removed": 0, "changed": 0}
    failures = 0
    for pkg_id, cfg in config.items():
        if args.only and pkg_id not in args.only:
            continue
        try:
            res = sync_package(pkg_id, cfg, args, report)
        except Exception as exc:  # keep going: one broken spec must not hide the others
            failures += 1
            report += [f"### {pkg_id}", f"- ERROR: {exc}", ""]
            continue
        if res["skipped"]:
            report += [f"### {pkg_id}", f"- skipped: {res['skipped']}", ""]
        for key in totals:
            totals[key] += res[key]
    summary = f"Totals: {totals['added']} added, {totals['removed']} removed from spec{' (pruned)' if args.prune else ''}, {totals['changed']} with changed parameters."
    report.insert(2, summary + "\n")
    text = "\n".join(report)
    sys.stdout.reconfigure(encoding="utf-8")
    print(text)
    if args.report:
        Path(args.report).write_text(text, encoding="utf-8")
    if failures:
        return 1
    drift = totals["added"] or totals["changed"] or totals["removed"]
    return EXIT_CHANGED if drift else 0


if __name__ == "__main__":
    sys.exit(main())
