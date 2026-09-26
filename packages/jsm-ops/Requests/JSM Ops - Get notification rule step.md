---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/notification-rule-steps
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/notification-rules/{ruleId}/steps/{id}"
category: "Notification rule steps"
writes_data: false
---
# JSM Ops - Get notification rule step

**Get notification rule step** — `GET /api/{cloudId}/v1/notification-rules/{ruleId}/steps/{id}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get notification rule step"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/notification-rules/{{param:ruleId}}/steps/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `ruleId` (path, string, required) — Identifier of the notification rule.
- `id` (path, string, required) — Identifier of the notification rule step which belongs to given notification rule.

## Original description

Gets a notification rule step with given id in the request.
