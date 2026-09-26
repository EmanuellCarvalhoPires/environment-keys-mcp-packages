---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/notification-rule-steps
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/notification-rules/{ruleId}/steps/{id}"
category: "Notification rule steps"
writes_data: true
---
# JSM Ops - Delete notification rule step

**Delete notification rule step** — `DELETE /api/{cloudId}/v1/notification-rules/{ruleId}/steps/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete notification rule step"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/notification-rules/{{param:ruleId}}/steps/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `ruleId` (path, string, required) — Identifier of the notification rule.
- `id` (path, string, required) — Identifier of the notification rule step which belongs to given notification rule.

## Original description

Deletes a notification rule step with given id in the request.
