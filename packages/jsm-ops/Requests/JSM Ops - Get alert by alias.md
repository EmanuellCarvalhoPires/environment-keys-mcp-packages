---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/alerts
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/alerts/alias"
category: "Alerts"
writes_data: false
---
# JSM Ops - Get alert by alias

**Get alert by alias** — `GET /api/{cloudId}/v1/alerts/alias`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get alert by alias"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/alias?alias={{param:alias}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `alias` (query, string, required) — Alias of the requested alert.

## Original description

This endpoint provides users the ability to retrieve comprehensive details of a specific alert using its unique alias as a query parameter.
