---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/alerts
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/alerts/{id}"
category: "Alerts"
writes_data: true
---
# JSM Ops - Delete alert

**Delete alert** — `DELETE /api/{cloudId}/v1/alerts/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete alert"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Identifier of the alert.

## Original description

This endpoint is utilized to delete alerts, along with the unique identifier of the alert.
