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
path: "/api/{cloudId}/v1/alerts/{alertId}/notes/{id}"
category: "Alerts"
writes_data: true
---
# JSM Ops - Delete alert note

**Delete alert note** — `DELETE /api/{cloudId}/v1/alerts/{alertId}/notes/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete alert note"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:alertId}}/notes/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `alertId` (path, string, required) — Identifier of the alert.
- `id` (path, string, required) — Identifier of the note.

## Original description

This endpoint is used to delete a note from an existing alert.
