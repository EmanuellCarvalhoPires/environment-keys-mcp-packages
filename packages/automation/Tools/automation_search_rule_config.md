---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/search
  - api/effect/read
up: "[[MCP - Automation]]"
tool: automation_search_rule_config
title: "Automation - Search rule configuration"
kind: script
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Finds which Automation rules contain a text in their configuration (trigger, conditions, actions and nested branches) and returns only the matching rules, with the component type and a snippet around each hit. Use it to answer 'which rule edits field X / uses smart value Y / calls URL Z?', e.g. text 'USE_REPORTER_EMAIL' in project ABC. Rules usually reference fields by NAME, not by id, so search both: 'customfield_10002|Organizations'. Filter by project whenever possible: it fetches the configuration of each candidate rule (one request per rule, capped by max_rules). Writes data: no."
params:
  "text":
    type: string
    required: true
    description: "Text to find in the rule configuration, case-insensitive. Several terms separated by | match any of them. For fields, include the field name and the id, e.g. 'Organizations|customfield_10002'."
  "product":
    type: string
    enum: ["jira", "confluence"]
    default: "jira"
    description: "Product where the rules run: jira (default) or confluence."
  "project":
    type: string
    description: "Jira project key or id to limit the candidate rules by scope, e.g. ABC. Strongly recommended."
  "include_global":
    type: boolean
    default: true
    description: "Also check global (site-wide) rules and rules scoped to the project's type (e.g. all service management projects). Default true."
  "state":
    type: string
    enum: ["ENABLED", "DISABLED"]
    description: "Only check rules in this state. Omit for both."
  "name":
    type: string
    description: "Only check rules whose name contains this fragment (case- and accent-insensitive)."
  "max_rules":
    type: integer
    default: 150
    description: "Maximum number of candidate rules whose configuration is fetched. Default 150. The result says how many were left out."
writes: false
expose: true
---
# automation_search_rule_config

Searches for a text **inside the configuration** of Automation rules: trigger, conditions, actions and nested branches. Returns only the rules where the text appears. Use it to find a rule by what it does when its name does not help (e.g. the rule that fills Organizations may be named after approvals or contracts).

- Requests: [[Automation - List rule summaries]], [[Automation - Get a rule by UUID]] (with `redactSensitiveFields=true`, so hidden web request headers are not returned) and [[Jira v3 - Get project]]. The last one comes from the Jira Cloud package: without it, the script calls `GET /rest/api/3/project/{key}` directly with the `url` and `auth_token` of the instance note.
- Instance: `instance` parameter (notes tagged `atlassian/instance`).
- Writes data: no.
- To only list rules by project, name or state, use [[automation_find_rules]], which is much faster.

## How it works

1. Lists the candidate rules with the same filters as [[automation_find_rules]] (`project`, `include_global`, `state`, `name`).
2. Fetches the configuration of each candidate, up to `max_rules`.
3. Walks the components and looks for each term of `text` (separated by `|`, case-insensitive).
4. If the term is somewhere else in the configuration, outside the components, the hit shows `where: "rule"`.

> [!tip] Fields by name
> Rules usually store a field by its **name** (`{"type":"NAME","value":"Organizations"}`), not by its id. Search both: `Organizations|customfield_10002`. Searching only for the id can miss the rule that edits the field.

## Result

`{ instance, product, project, terms, candidates, checked, not_checked, count, matches: [{ name, uuid, state, scope, updated, hits: [{ where, component, type, term, snippet }] }], errors? }`

- `where`: position of the component. `trigger` is the trigger, `3` is the 3rd top-level component, `3.2` is its 2nd child, `3.cond1` is its 1st condition.
- `component` / `type`: component kind (`TRIGGER`, `CONDITION`, `ACTION`, `BRANCH`...) and technical type (e.g. `jira.issue.edit`).
- `snippet`: about 120 characters of the configuration around the term.

```js
const GET_PROJECT_REQUEST = "Jira v3 - Get project";
const SNIPPET_RADIUS = 60;

// Jira projectTypeKey -> owner of the ARI of project-type rules (ari:cloud:<owner>::site/<cloud_id>)
const TYPE_OWNERS = {
  software: "jira-software",
  service_desk: "jira-servicedesk",
  business: "jira-core",
  product_discovery: "jira-product-discovery",
  customer_service: "jira-customer-service",
};

function norm(value) {
  let s = String(value ?? "").toLowerCase();
  try { s = s.normalize("NFD").replace(/[̀-ͯ]/g, ""); } catch (e) { /* no normalize */ }
  return s;
}

// Brasília = UTC-3 (no daylight saving time since 2019)
function fmtDate(epochSeconds) {
  if (epochSeconds == null) return null;
  const d = new Date(Math.round(Number(epochSeconds) * 1000) - 3 * 3600 * 1000);
  const p = (n) => String(n).padStart(2, "0");
  return `${p(d.getUTCDate())}/${p(d.getUTCMonth() + 1)}/${d.getUTCFullYear()} ${p(d.getUTCHours())}:${p(d.getUTCMinutes())}`;
}

// Uses the Jira Cloud request note when it is in the vault; otherwise calls the endpoint
// with the url and auth_token of the instance note.
async function getProject(ctx, project) {
  try {
    return await ctx.requests.run(GET_PROJECT_REQUEST, { projectIdOrKey: String(project) });
  } catch (e) {
    const fm = ctx.service?.frontmatter ?? {};
    if (!fm.url || !fm.auth_token) throw e;
    return await ctx.http({
      method: "GET",
      url: `${String(fm.url).replace(/\/+$/, "")}/rest/api/3/project/${encodeURIComponent(String(project))}`,
      headers: { Authorization: String(fm.auth_token), Accept: "application/json" },
    });
  }
}

async function resolveProject(ctx, project) {
  const r = await getProject(ctx, project);
  if (!r.ok || !r.json?.id) {
    throw new Error(`Project "${project}" not found (HTTP ${r.status}).`);
  }
  return { id: String(r.json.id), key: r.json.key, name: r.json.name, typeKey: r.json.projectTypeKey ?? null };
}

// The API cursor pagination skips and repeats rules between pages: a large page usually
// brings everything at once, and each uuid is kept only once if more pages are still needed.
async function listAllRules(ctx, product) {
  const rules = [];
  const seen = new Set();
  let cursor = null;
  let pages = 0;
  while (pages < 200) {
    const params = { product, limit: "1000" };
    if (cursor) params.cursor = cursor;
    const r = await ctx.requests.run("Automation - List rule summaries", params);
    if (!r.ok || !r.json) {
      return { rules, pages, error: `HTTP ${r.status} on page ${pages + 1}${r.truncated ? " (response truncated)" : ""}`, details: r.json ?? r.body };
    }
    for (const rule of r.json?.data ?? []) {
      if (seen.has(rule.uuid)) continue;
      seen.add(rule.uuid);
      rules.push(rule);
    }
    pages++;
    const next = r.json?.links?.next;
    const m = next ? /[?&]cursor=([^&]+)/.exec(next) : null;
    if (!m) break;
    try { cursor = decodeURIComponent(m[1]); } catch (e) { cursor = m[1]; }
  }
  return { rules, pages };
}

// Global = jira::site or confluence::site. <type>::site only applies to projects of that type.
function scopeInfo(aris, target) {
  const scopes = [];
  let inProject = false;
  let isGlobal = false;
  let isType = false;
  let inType = false;
  for (const ari of aris ?? []) {
    const pm = /:project\/(\d+)$/.exec(ari);
    const sm = /^ari:cloud:([^:]+)::site\//.exec(ari);
    if (pm) {
      if (target && pm[1] === target.id) {
        inProject = true;
        scopes.push(target.key);
      } else {
        scopes.push(`project/${pm[1]}`);
      }
    } else if (sm && (sm[1] === "jira" || sm[1] === "confluence")) {
      isGlobal = true;
      scopes.push("global");
    } else if (sm) {
      isType = true;
      scopes.push(`type:${sm[1]}`);
      // Unknown project type: keep the rule, so one that may apply is not hidden
      const owner = target ? TYPE_OWNERS[target.typeKey] : null;
      if (target && (!owner || owner === sm[1])) inType = true;
    } else {
      scopes.push(ari);
    }
  }
  return { scopes: [...new Set(scopes)], inProject, isGlobal, isType, inType };
}

function snippetAt(text, index, length) {
  const start = Math.max(0, index - SNIPPET_RADIUS);
  const end = Math.min(text.length, index + length + SNIPPET_RADIUS);
  return (start > 0 ? "…" : "") + text.slice(start, end) + (end < text.length ? "…" : "");
}

function findHits(text, terms) {
  const lower = text.toLowerCase();
  const hits = [];
  for (const term of terms) {
    const i = lower.indexOf(term.toLowerCase());
    if (i >= 0) hits.push({ term, snippet: snippetAt(text, i, term.length) });
  }
  return hits;
}

// Walks the trigger and the components (with their conditions and children) and looks for
// the terms in each component's own content
function searchComponents(rule, terms) {
  const hits = [];
  const visit = (node, where) => {
    if (!node || typeof node !== "object") return;
    const own = {};
    for (const k of Object.keys(node)) {
      if (k !== "children" && k !== "conditions") own[k] = node[k];
    }
    for (const h of findHits(JSON.stringify(own), terms)) {
      hits.push({ where, component: node.component ?? null, type: node.type ?? null, ...h });
    }
    (node.conditions ?? []).forEach((c, i) => visit(c, `${where}.cond${i + 1}`));
    (node.children ?? []).forEach((c, i) => visit(c, `${where}.${i + 1}`));
  };
  if (rule.trigger) visit(rule.trigger, "trigger");
  (rule.components ?? []).forEach((c, i) => visit(c, String(i + 1)));
  return hits;
}

export default async function (ctx) {
  const { text, product, project, include_global, state, name, max_rules } = ctx.args;

  const terms = String(text).split("|").map((t) => t.trim()).filter(Boolean);
  if (!terms.length) return { error: "Provide at least one term in text." };
  if (project && product !== "jira") {
    return { error: "The project filter only applies to product = jira." };
  }

  let target = null;
  if (project) {
    try {
      target = await resolveProject(ctx, project);
    } catch (e) {
      return { error: String(e.message ?? e) };
    }
  }

  const listed = await listAllRules(ctx, product);
  if (listed.error && listed.rules.length === 0) {
    return { error: listed.error, details: listed.details };
  }

  const nameQ = name ? norm(name) : null;
  const candidates = [];
  for (const rule of listed.rules) {
    const info = scopeInfo(rule.ruleScopeARIs, target);
    const wideOnly = (info.isGlobal || info.isType) && !info.inProject;
    if (target && !info.inProject && !(include_global && (info.isGlobal || info.inType))) continue;
    if (!target && !include_global && wideOnly) continue;
    if (state && rule.state !== state) continue;
    if (nameQ && !norm(rule.name).includes(nameQ)) continue;
    candidates.push({ rule, scope: info.scopes.join(", ") });
  }

  const limit = Math.max(1, Number(max_rules) || 150);
  const toCheck = candidates.slice(0, limit);
  const matches = [];
  const errors = [];

  for (const { rule, scope } of toCheck) {
    const r = await ctx.requests.run("Automation - Get a rule by UUID", {
      product,
      ruleUuid: rule.uuid,
      redactSensitiveFields: "true",
    });
    if (!r.ok || !r.json) {
      errors.push({ name: rule.name, uuid: rule.uuid, error: `HTTP ${r.status}` });
      continue;
    }
    if (r.truncated) {
      errors.push({ name: rule.name, uuid: rule.uuid, error: "response truncated by the plugin; check it with automation_get_a_rule_by_uuid" });
    }
    const config = r.json.rule ?? r.json;
    let hits = searchComponents(config, terms);
    if (!hits.length) {
      // Term outside the components (e.g. the description or other rule metadata)
      hits = findHits(JSON.stringify(config), terms).map((h) => ({ where: "rule", component: null, type: null, ...h }));
    }
    if (hits.length) {
      matches.push({
        name: String(rule.name ?? "").trim(),
        uuid: rule.uuid,
        state: rule.state,
        scope,
        updated: fmtDate(rule.updated),
        hits,
      });
    }
  }

  const result = {
    instance: ctx.args.instance,
    product,
    project: target ? `${target.key} (${target.id}, ${target.typeKey}) - ${target.name}` : null,
    terms,
    candidates: candidates.length,
    checked: toCheck.length,
    not_checked: candidates.length - toCheck.length,
    count: matches.length,
    matches,
  };
  if (errors.length) result.errors = errors;
  if (listed.error) result.warning = `Incomplete listing: ${listed.error}`;
  if (result.not_checked > 0) {
    result.warning = [result.warning, `${result.not_checked} rule(s) not checked: narrow the filters or raise max_rules.`].filter(Boolean).join(" ");
  }
  return result;
}
```
