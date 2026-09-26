---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-roles
  - api/operation/action
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/spaces/{id}/role-assignments"
category: "Space Roles"
writes_data: true
tool_note: "[[confluence_set_space_role_assignments]]"
---
# Confluence v2 - Set space role assignments

**Set space role assignments** — `POST /spaces/{id}/role-assignments`

- Run by the tool [[confluence_set_space_role_assignments]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/spaces/{{param:id}}/role-assignments
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the space for which to retrieve assignments.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Sets space role assignments as specified in the payload. For each entry, if `roleId` is provided
the principal is assigned to that role. If `roleId` is omitted, the role assignment for that principal is removed, if it exists.

Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to manage roles in the space.
