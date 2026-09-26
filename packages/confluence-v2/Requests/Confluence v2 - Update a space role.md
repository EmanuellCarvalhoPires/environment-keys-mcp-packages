---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-roles
  - api/operation/update
  - api/effect/write
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: PUT
path: "/space-roles/{id}"
category: "Space Roles"
writes_data: true
tool_note: "[[confluence_update_a_space_role]]"
---
# Confluence v2 - Update a space role

**Update a space role** — `PUT /space-roles/{id}`

- Run by the tool [[confluence_update_a_space_role]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
PUT {{service.url}}/wiki/api/v2/space-roles/{{param:id}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Id of the space role
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update a space role.

Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
User must be an organization or site admin. Connect and Forge app users are not authorized to access this resource.
