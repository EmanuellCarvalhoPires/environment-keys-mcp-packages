---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-permissions
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/spaces/{id}/permissions"
category: "Space Permissions"
writes_data: false
tool_note: "[[confluence_get_space_permissions_assignments]]"
---
# Confluence v2 - Get space permissions assignments

**Get space permissions assignments** — `GET /spaces/{id}/permissions`

- Run by the tool [[confluence_get_space_permissions_assignments]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/spaces/{{param:id}}/permissions?cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the space to be returned.
- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of assignments to return. If more results exist, use the Link response header to retrieve a relative URL that will return the next set of results.

## Original description

Returns space permission assignments for a specific space.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the space.
