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
path: "/api/{cloudId}/v1/alerts/{id}/assign"
category: "Alerts"
writes_data: true
---
# JSM Ops - Assign alert

**Assign alert** — `POST /api/{cloudId}/v1/alerts/{id}/assign`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Assign alert"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/alerts/{{param:id}}/assign
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Identifier of the alert.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

This endpoint is used to assign an existing alert to a user or a group. Assigning an alert ensures that responsibility for addressing the alert is clearly established, promoting efficient alert management and quicker resolution times. It is a crucial operation for coordinating incident response efforts effectively.
