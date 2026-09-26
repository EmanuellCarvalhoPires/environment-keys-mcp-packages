---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/alerts
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/alerts/{id}"
category: "Alerts"
writes_data: false
---
# JSM Ops - Get alert

**Get alert** — `GET /api/{cloudId}/v1/alerts/{id}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get alert"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Identifier of the alert.

## Original description

This endpoint provides users the ability to retrieve comprehensive details of a specific alert using its unique id.
