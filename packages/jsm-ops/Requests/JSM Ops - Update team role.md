---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/team-roles
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: PATCH
path: "/api/{cloudId}/v1/teams/{teamId}/roles/{identifier}"
category: "Team roles"
writes_data: true
---
# JSM Ops - Update team role

**Update team role** — `PATCH /api/{cloudId}/v1/teams/{teamId}/roles/{identifier}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update team role"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
PATCH https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/roles/{{param:identifier}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `teamId` (path, string, required) — Id of the team.
- `identifier` (path, string, required) — Id of the team role.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the details of a team role
