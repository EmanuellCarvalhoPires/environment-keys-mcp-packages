---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-roles
  - api/operation/create
  - api/effect/write
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/space-roles"
category: "Space Roles"
writes_data: true
tool_note: "[[confluence_create_a_space_role]]"
---
# Confluence v2 - Create a space role

**Create a space role** — `POST /space-roles`

- Run by the tool [[confluence_create_a_space_role]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/space-roles
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create a space role.

Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
User must be an organization or site admin. Connect and Forge app users are not authorized to access this resource.
