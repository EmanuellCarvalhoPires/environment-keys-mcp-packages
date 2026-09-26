---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-roles
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/space-roles/{id}"
category: "Space Roles"
writes_data: false
tool_note: "[[confluence_get_space_role_by_id]]"
---
# Confluence v2 - Get space role by ID

**Get space role by ID** — `GET /space-roles/{id}`

- Run by the tool [[confluence_get_space_role_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/space-roles/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the space role to retrieve.

## Original description

Retrieves the space role by ID.

Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site.
