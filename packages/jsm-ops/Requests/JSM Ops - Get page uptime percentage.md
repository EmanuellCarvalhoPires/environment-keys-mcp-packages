---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/status-page
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/uptime_percentage"
category: "Status Page"
writes_data: false
---
# JSM Ops - Get page uptime percentage

**Get page uptime percentage** — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/uptime_percentage`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get page uptime percentage"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/pages/{{param:pageId}}/uptime_percentage?from={{param:from}}&to={{param:to}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pageId` (path, string, required) — Identifier of the page.
- `from` (query, string, optional) — Start of the period (ISO-8601 date-time).
- `to` (query, string, optional) — End of the period (ISO-8601 date-time).

## Original description

Get the uptime percentage for a status page over a given period.
