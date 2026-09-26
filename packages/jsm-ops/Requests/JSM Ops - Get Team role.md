---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/team-roles
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/teams/{teamId}/roles/{identifier}"
category: "Team roles"
writes_data: false
---
# JSM Ops - Get Team role

**Get Team role** — `GET /api/{cloudId}/v1/teams/{teamId}/roles/{identifier}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Get Team role"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/roles/{{param:identifier}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `teamId` (path, string, required) — Identifier of the team.
- `identifier` (path, string, required) — Identifier of the team role.

## Original description

Returns details of a team role.
