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
path: "/api/{cloudId}/v1/alerts/{alertId}/attachments/{id}"
category: "Alerts"
writes_data: true
---
# JSM Ops - Delete attachment

**Delete attachment** — `DELETE /api/{cloudId}/v1/alerts/{alertId}/attachments/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete attachment"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:alertId}}/attachments/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `alertId` (path, string, required) — The ID of the alert.
- `id` (path, string, required) — The attachment ID (timestamp).

## Original description

Deletes the specified attachment from the alert.
