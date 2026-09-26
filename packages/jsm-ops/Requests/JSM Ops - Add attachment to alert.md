---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/alerts
  - api/operation/create
  - api/effect/write
  - api/format/multipart
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/alerts/{alertId}/attachments"
category: "Alerts"
writes_data: true
---
# JSM Ops - Add attachment to alert

**Add attachment to alert** — `POST /api/{cloudId}/v1/alerts/{alertId}/attachments`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Add attachment to alert"`.
- **Format:** the endpoint expects `multipart/form-data` (file upload), which the plugin `http` block cannot build. Kept as reference.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:alertId}}/attachments
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `alertId` (path, string, required) — The ID of the alert.

## Original description

Adds a file attachment to an alert.
