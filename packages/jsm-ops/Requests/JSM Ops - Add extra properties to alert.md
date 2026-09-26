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
path: "/api/{cloudId}/v1/alerts/{id}/extra-properties"
category: "Alerts"
writes_data: true
---
# JSM Ops - Add extra properties to alert

**Add extra properties to alert** — `POST /api/{cloudId}/v1/alerts/{id}/extra-properties`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Add extra properties to alert"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:id}}/extra-properties
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Identifier of the alert.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

This endpoint is used to enrich existing alerts with additional information to provide more detailed context.
