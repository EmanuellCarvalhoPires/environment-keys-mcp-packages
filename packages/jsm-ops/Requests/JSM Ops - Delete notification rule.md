---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/notification-rules
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/notification-rules/{id}"
category: "Notification rules"
writes_data: true
---
# JSM Ops - Delete notification rule

**Delete notification rule** — `DELETE /api/{cloudId}/v1/notification-rules/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete notification rule"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/notification-rules/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Identifier of the notification rule

## Original description

Deletes a notification rule with given id in the request.
