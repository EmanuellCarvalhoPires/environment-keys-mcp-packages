---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/notification-rules
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/notification-rules"
category: "Notification rules"
writes_data: true
---
# JSM Ops - Create notification rule

**Create notification rule** — `POST /api/{cloudId}/v1/notification-rules`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create notification rule"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/notification-rules
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a notification rule with the given properties for the user.
