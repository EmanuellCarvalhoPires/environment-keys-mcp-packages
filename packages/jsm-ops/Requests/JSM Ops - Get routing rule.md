---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/routing-rules
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/teams/{teamId}/routing-rules/{id}"
category: "Routing rules"
writes_data: false
---
# JSM Ops - Get routing rule

**Get routing rule** — `GET /api/{cloudId}/v1/teams/{teamId}/routing-rules/{id}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get routing rule"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/routing-rules/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `teamId` (path, string, required) — Identifier of the routing rules owning team.
- `id` (path, string, required) — Identifier of the routing rule.

## Original description

Gets a routing rule with given id in the request.
