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
path: "/space-permissions"
category: "Space Permissions"
writes_data: false
tool_note: "[[confluence_get_available_space_permissions]]"
---
# Confluence v2 - Get available space permissions

**Get available space permissions** — `GET /space-permissions`

- Run by the tool [[confluence_get_available_space_permissions]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/space-permissions?cursor={{param:cursor}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `cursor` (query, string, optional) — Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results.
- `limit` (query, string, optional) — Maximum number of space permissions to return. If more results exist, use the Link response header to retrieve a relative URL that will return the next set of results.

## Original description

Retrieves the available space permissions.

Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site.
