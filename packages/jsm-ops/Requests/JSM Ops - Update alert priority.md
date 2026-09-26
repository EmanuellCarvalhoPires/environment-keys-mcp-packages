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
path: "/api/{cloudId}/v1/alerts/{id}/priority"
category: "Alerts"
writes_data: true
---
# JSM Ops - Update alert priority

**Update alert priority** — `PATCH /api/{cloudId}/v1/alerts/{id}/priority`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update alert priority"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PATCH https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:id}}/priority
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Identifier of the alert.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

This endpoint is used to modify the priority level of an existing alert. This endpoint allows for dynamic control over alert urgency. This aids in effective incident management by ensuring the most critical issues are addressed first.
