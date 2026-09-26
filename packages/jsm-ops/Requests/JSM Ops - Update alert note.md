---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/alerts
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PATCH
path: "/api/{cloudId}/v1/alerts/{alertId}/notes/{id}"
category: "Alerts"
writes_data: true
---
# JSM Ops - Update alert note

**Update alert note** — `PATCH /api/{cloudId}/v1/alerts/{alertId}/notes/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update alert note"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PATCH https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:alertId}}/notes/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `alertId` (path, string, required) — Identifier of the alert.
- `id` (path, string, required) — Identifier of the note.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

This endpoint is used to update a note associated with a specific alert.
