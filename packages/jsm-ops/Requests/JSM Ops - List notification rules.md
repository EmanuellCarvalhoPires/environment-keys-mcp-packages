---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/notification-rules
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/notification-rules"
category: "Notification rules"
writes_data: false
---
# JSM Ops - List notification rules

**List notification rules** — `GET /api/{cloudId}/v1/notification-rules`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List notification rules"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/notification-rules?offset={{param:offset}}&size={{param:size}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `offset` (query, string, optional) — The offset parameter controls the starting point within the collection of resource results.
- `size` (query, string, optional) — The size parameter controls the maximum number of items that may be returned for a single request.

## Original description

Lists all notification rules for the user. It optionally takes two parameters - offset and size.
