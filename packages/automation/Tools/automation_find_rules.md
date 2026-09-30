---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/search
  - api/effect/read
up: "[[MCP - Automation]]"
tool: automation_find_rules
title: "Automation - Find rules (filtered)"
kind: script
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Finds Automation rules and returns a compact list (name, uuid, state, scope, labels, last update in Brasília time). Pages through GET /rest/v1/rule/summary internally and filters by Jira project (key or id, e.g. ABC), global and project-type rules, state, name fragment and label. Use it instead of automation_list_rule_summaries whenever you need the rules of a project or with a given name/state, e.g. 'which automations run in project ABC?'. Writes data: no."
params:
  "product":
    type: string
    enum: ["jira", "confluence"]
    default: "jira"
    description: "Product where the rules run: jira (default) or confluence."
  "project":
    type: string
    description: "Jira project key or id to filter by rule scope, e.g. ABC or 10001. Omit to search all rules."
  "include_global":
    type: boolean
    default: true
    description: "Also include global (site-wide) rules and rules scoped to a project type (e.g. all service management projects). Default true. With a project, returns the project's rules plus the global ones and the ones of its project type; without a project and false, hides global and project-type rules."
  "state":
    type: string
    enum: ["ENABLED", "DISABLED"]
    description: "Only rules in this state. Omit for both."
  "name":
    type: string
    description: "Fragment of the rule name, case- and accent-insensitive, e.g. 'organization' or 'approver'."
  "label":
    type: string
    description: "Fragment of a rule label, case- and accent-insensitive, e.g. 'Validation'."
  "page_size":
    type: integer
    default: 1000
    description: "Rules per API page. Default 1000, which usually brings every rule in a single page: the API cursor pagination skips and repeats rules between pages. Only change it to diagnose pagination."
writes: false
expose: true
---
# automation_find_rules

Finds Automation rules with filters and returns only the essentials of each one. The pagination of `GET /rest/v1/rule/summary` happens inside the script, so one call replaces several raw pages of [[automation_list_rule_summaries]].

- Requests: [[Automation - List rule summaries]] and [[Jira v3 - Get project]] (turns the project key into its id and type). The second one comes from the Jira Cloud package: without it, the script calls `GET /rest/api/3/project/{key}` directly with the `url` and `auth_token` of the instance note.
- Instance: `instance` parameter (notes tagged `atlassian/instance`).
- Writes data: no.
- To search by what a rule does (field, action, configuration text), use [[automation_search_rule_config]].

## Filters

| Parameter | Effect |
| --- | --- |
| `project` | Rules whose scope includes the project (`...:project/<id>`), including multi-project rules. |
| `include_global` | Adds the global rules (`jira::site/` scope) and the project-type rules (`<type>::site/` scope, e.g. all service management projects). With `project`, only the rules of that project's type. Default `true`. |
| `state` | `ENABLED` or `DISABLED`. |
| `name` / `label` | Fragment of the name or of a label, case- and accent-insensitive. |
| `page_size` | Rules per API page. Default 1000, which usually brings everything in a single page: the API cursor pagination skips and repeats rules between pages (on an instance with about 850 rules: 848 rules with pages of 50, 852 with 100 and 854 with 1000). Only change it to diagnose pagination. |

## Result

`{ instance, product, project, filters, scanned, pages, count, rules: [{ name, uuid, state, scope, labels?, updated }] }`

- `scope`: the key of the filtered project, `global`, `type:<type>` for the rules of a project type (e.g. `type:jira-software`) or `project/<id>` for other projects.
- `updated`: date of the last change in Brasília time (UTC-3, `dd/MM/yyyy HH:mm`).

```js
const GET_PROJECT_REQUEST = "Jira v3 - Get project";

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

// The API cursor pagination skips and repeats rules between pages (tested: 848 rules with
// pages of 50, 852 with 100 and 854 in a single page of 1000). That is why the default is a
// large page, and each uuid is kept only once in case the listing still needs more pages.
async function listAllRules(ctx, product, pageSize) {
  const rules = [];
  const seen = new Set();
  let cursor = null;
  let pages = 0;
  while (pages < 500) {
    const params = { product, limit: String(pageSize) };
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

export default async function (ctx) {
  const { product, project, include_global, state, name, label, page_size } = ctx.args;

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

  const listed = await listAllRules(ctx, product, Math.max(1, Number(page_size) || 1000));
  if (listed.error && listed.rules.length === 0) {
    return { error: listed.error, details: listed.details };
  }

  const nameQ = name ? norm(name) : null;
  const labelQ = label ? norm(label) : null;

  const rules = [];
  for (const rule of listed.rules) {
    const info = scopeInfo(rule.ruleScopeARIs, target);
    const wideOnly = (info.isGlobal || info.isType) && !info.inProject;

    if (target && !info.inProject && !(include_global && (info.isGlobal || info.inType))) continue;
    if (!target && !include_global && wideOnly) continue;
    if (state && rule.state !== state) continue;
    if (nameQ && !norm(rule.name).includes(nameQ)) continue;
    if (labelQ && !(rule.labels ?? []).some((l) => norm(l).includes(labelQ))) continue;

    const row = {
      name: String(rule.name ?? "").trim(),
      uuid: rule.uuid,
      state: rule.state,
      scope: info.scopes.join(", "),
      updated: fmtDate(rule.updated),
    };
    if (rule.labels?.length) row.labels = rule.labels;
    rules.push(row);
  }

  rules.sort((a, b) => a.name.localeCompare(b.name));

  const result = {
    instance: ctx.args.instance,
    product,
    project: target ? `${target.key} (${target.id}, ${target.typeKey}) - ${target.name}` : null,
    filters: { include_global, state: state ?? null, name: name ?? null, label: label ?? null },
    scanned: listed.rules.length,
    pages: listed.pages,
    count: rules.length,
    rules,
  };
  if (listed.error) result.warning = `Incomplete listing: ${listed.error}`;
  return result;
}
```
