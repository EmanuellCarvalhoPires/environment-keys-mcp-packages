---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/alerts
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/alerts/{id}/responders"
category: "Alerts"
writes_data: true
---
# JSM Ops - Add responder to alert

**Add responder to alert** — `POST /api/{cloudId}/v1/alerts/{id}/responders`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Add responder to alert"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:id}}/responders
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Identifier of the alert.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

This endpoint is used to assign a responder to an existing alert. The responder is the individual or team responsible for addressing the alert. This operation streamlines the alert management process by ensuring that alerts are directed to the correct parties for timely resolution.
