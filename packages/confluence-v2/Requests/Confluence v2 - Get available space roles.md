---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-roles
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/space-roles"
category: "Space Roles"
writes_data: false
tool_note: "[[confluence_get_available_space_roles]]"
---
# Confluence v2 - Get available space roles

**Get available space roles** — `GET /space-roles`

- Run by the tool [[confluence_get_available_space_roles]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/space-roles?space-id={{param:space_id}}&role-type={{param:role_type}}&principal-id={{param:principal_id}}&principal-type={{param:principal_type}}&cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `space_id` (query, string, optional) — The space ID for which to filter available space roles; if empty, return all available space roles for the tenant.
- `role_type` (query, string, optional) — The space role type to filter results by.
- `principal_id` (query, string, optional) — The principal ID to filter results by. If specified, a principal-type must also be specified.
- `principal_type` (query, string, optional) — The principal type to filter results by. If specified, a principal-id must also be specified.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of space roles to return. If more results exist, use the Link response header to retrieve a relative URL that will return the next set of results.

## Original description

Retrieves the available space roles.

Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site; if requesting a certain space's roles, permission to view the space.
