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
path: "/api/{cloudId}/v1/alerts/{id}/snooze"
category: "Alerts"
writes_data: true
---
# JSM Ops - Snooze alert

**Snooze alert** — `POST /api/{cloudId}/v1/alerts/{id}/snooze`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Snooze alert"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:id}}/snooze
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Identifier of the alert.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

This endpoint is used to snooze an existing alert. The snooze operation temporarily silences the alert, preventing it from triggering notifications for a specified period. This is particularly useful for managing alerts that require attention at a later time or to reduce noise from non-critical alerts.
