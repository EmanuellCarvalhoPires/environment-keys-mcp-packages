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
path: "/spaces/{id}/role-assignments"
category: "Space Roles"
writes_data: false
tool_note: "[[confluence_get_space_role_assignments]]"
---
# Confluence v2 - Get space role assignments

**Get space role assignments** — `GET /spaces/{id}/role-assignments`

- Run by the tool [[confluence_get_space_role_assignments]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/spaces/{{param:id}}/role-assignments?role-id={{param:role_id}}&role-type={{param:role_type}}&principal-id={{param:principal_id}}&principal-type={{param:principal_type}}&cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the space for which to retrieve assignments.
- `role_id` (query, string, optional) — Filters the returned role assignments to the provided role ID.
- `role_type` (query, string, optional) — Filters the returned role assignments to the provided role type.
- `principal_id` (query, string, optional) — Filters the returned role assignments to the provided principal id. If specified, a principal-type must also be specified.
- `principal_type` (query, string, optional) — Filters the returned role assignments to the provided principal type. If specified, a principal-id must also be specified.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of space roles to return. If more results exist, use the Link response header to retrieve a relative URL that will return the next set of results.

## Original description

Retrieves the space role assignments.

Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the space.
