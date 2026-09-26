---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/team-roles
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: DELETE
path: "/api/{cloudId}/v1/teams/{teamId}/roles/{identifier}"
category: "Team roles"
writes_data: true
---
# JSM Ops - Delete a team role

**Delete a team role.** — `DELETE /api/{cloudId}/v1/teams/{teamId}/roles/{identifier}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete a team role"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
DELETE https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/teams/{{param:teamId}}/roles/{{param:identifier}}
Authorization: {{service.auth_token}}
```

## Parameters

- `teamId` (path, string, required) — Id of the team.
- `identifier` (path, string, required) — Id of the custom user role.

## Original description

Deletes a team role.
