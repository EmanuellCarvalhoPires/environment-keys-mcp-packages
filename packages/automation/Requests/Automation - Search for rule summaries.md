---
tags:
  - api/request
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/search
  - api/effect/read
up: "[[MCP - Automation]]"
app: "Automation"
method: POST
path: "/rest/v1/rule/summary"
category: "Rule management"
writes_data: false
tool_note: "[[automation_search_for_rule_summaries]]"
---
# Automation - Search for rule summaries

**Search for rule summaries** — `POST /rest/v1/rule/summary`

- Run by the tool [[automation_search_for_rule_summaries]].
- Official documentation: https://developer.atlassian.com/cloud/automation/rest/

```http
POST {{service.url}}/gateway/api/automation/public/{{param:product}}/{{service.cloud_id}}/rest/v1/rule/summary
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `product` (path, string, required) — Product where the rule runs: jira or confluence.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Get rule summaries for rules that match the given criteria via POST.

Supports filtering by trigger, rule state, and rule scope (single ARI).

**Deprecated:** The `links` field in the response body has recently changed to return just the query parameters instead of absolute links. See [the changelog notice](/cloud/automation/api/changelog/#1-august-2025).
