---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/alerts
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/alerts/{id}/close"
category: "Alerts"
writes_data: true
---
# JSM Ops - Close alert

**Close alert** — `POST /api/{cloudId}/v1/alerts/{id}/close`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Close alert"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:id}}/close
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Identifier of the alert.

## Original description

This endpoint is used to close an existing alert. Closing an alert indicates that the issue has been resolved and no further action is necessary. This operation is essential for maintaining an accurate overview of the operational status and for ensuring that only active, unresolved issues remain open.
