---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/routing-rules
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PATCH
path: "/api/{cloudId}/v1/teams/{teamId}/routing-rules/{id}/change-order"
category: "Routing rules"
writes_data: true
---
# JSM Ops - Change routing rule order

**Change routing rule order** — `PATCH /api/{cloudId}/v1/teams/{teamId}/routing-rules/{id}/change-order`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Change routing rule order"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PATCH https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/routing-rules/{{param:id}}/change-order
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `teamId` (path, string, required) — Identifier of the routing rules owning team.
- `id` (path, string, required) — Identifier of the routing rule.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Changes routing rule's order with given id in the request.
