---
tags:
  - api/request
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/list
  - api/effect/read
up: "[[MCP - Automation]]"
app: "Automation"
method: GET
path: "/rest/v1/rule/summary"
category: "Rule management"
writes_data: false
tool_note: "[[automation_list_rule_summaries]]"
---
# Automation - List rule summaries

**List rule summaries** — `GET /rest/v1/rule/summary`

- Run by the tool [[automation_list_rule_summaries]].
- Official documentation: https://developer.atlassian.com/cloud/automation/rest/

```http
GET {{service.url}}/gateway/api/automation/public/{{param:product}}/{{service.cloud_id}}/rest/v1/rule/summary?cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `product` (path, string, required) — Product where the rule runs: jira or confluence.
- `cursor` (query, string, optional) — The pagination cursor to use to fetch a page of results. The first call should be made without a cursor. Cursors are returned in the response body and should not be constructed manually.
- `limit` (query, string, optional) — Optional page size limit

## Original description

Get rule summaries for all rules.

**Deprecated:** The `links` field in the response body has recently changed to return just the query parameters instead of absolute links. See [the changelog notice](/cloud/automation/api/changelog/#1-august-2025).
