---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/notification-rule-steps
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/notification-rules/{ruleId}/steps"
category: "Notification rule steps"
writes_data: false
---
# JSM Ops - List notification rule steps

**List notification rule steps** — `GET /api/{cloudId}/v1/notification-rules/{ruleId}/steps`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List notification rule steps"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/notification-rules/{{param:ruleId}}/steps?offset={{param:offset}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `ruleId` (path, string, required) — Identifier of the notification rule
- `offset` (query, string, optional) — The offset parameter controls the starting point within the collection of resource results.
- `size` (query, string, optional) — The size parameter controls the maximum number of items that may be returned for a single request.

## Original description

Lists all notifaction rule steps for the user. It optionally takes two parameters - offset and size.
