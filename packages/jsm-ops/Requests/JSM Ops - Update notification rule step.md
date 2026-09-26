---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/notification-rule-steps
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PATCH
path: "/api/{cloudId}/v1/notification-rules/{ruleId}/steps/{id}"
category: "Notification rule steps"
writes_data: true
---
# JSM Ops - Update notification rule step

**Update notification rule step** — `PATCH /api/{cloudId}/v1/notification-rules/{ruleId}/steps/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update notification rule step"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PATCH https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/notification-rules/{{param:ruleId}}/steps/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `ruleId` (path, string, required) — Identifier of the notification rule.
- `id` (path, string, required) — Identifier of the notification rule step which belongs to given notification rule.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates a notification rule step with given id in the request.
