---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/routing-rules
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/api/{cloudId}/v1/teams/{teamId}/routing-rules"
category: "Routing rules"
writes_data: true
---
# JSM Ops - Create routing rule

**Create routing rule** — `POST /api/{cloudId}/v1/teams/{teamId}/routing-rules`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Create routing rule"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/routing-rules
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `teamId` (path, string, required) — Identifier of the routing rules owning team.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates a routing rule with the given properties.
