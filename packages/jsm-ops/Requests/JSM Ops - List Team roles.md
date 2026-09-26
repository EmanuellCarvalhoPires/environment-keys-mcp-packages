---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/team-roles
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/teams/{teamId}/roles"
category: "Team roles"
writes_data: false
---
# JSM Ops - List Team roles

**List Team roles** — `GET /api/{cloudId}/v1/teams/{teamId}/roles`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List Team roles"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/roles
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `teamId` (path, string, required) — Identifier of the team.

## Original description

Returns list of team roles.
