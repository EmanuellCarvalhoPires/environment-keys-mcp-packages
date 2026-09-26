---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/notification-rule-steps
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/notification-rules/{ruleId}/steps"
category: "Notification rule steps"
writes_data: true
---
# JSM Ops - Create notification rule step

**Create notification rule step** — `POST /api/{cloudId}/v1/notification-rules/{ruleId}/steps`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create notification rule step"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/notification-rules/{{param:ruleId}}/steps
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `ruleId` (path, string, required) — Identifier of the notification rule.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a notification rule step with the given properties.
