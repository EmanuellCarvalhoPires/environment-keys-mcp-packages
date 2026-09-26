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
path: "/api/{cloudId}/v1/alerts/{alertId}/attachments/{id}"
category: "Alerts"
writes_data: false
---
# JSM Ops - Get attachment download URL

**Get attachment download URL** — `GET /api/{cloudId}/v1/alerts/{alertId}/attachments/{id}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get attachment download URL"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:alertId}}/attachments/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `alertId` (path, string, required) — The ID of the alert.
- `id` (path, string, required) — The attachment ID (timestamp).

## Original description

Gets a temporary download URL for the specified attachment.
