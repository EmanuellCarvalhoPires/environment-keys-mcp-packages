---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/admin-key
  - api/operation/list
  - api/effect/read
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/admin-key"
category: "Admin Key"
writes_data: false
tool_note: "[[confluence_get_admin_key]]"
---
# Confluence v2 - Get Admin Key

**Get Admin Key** — `GET /admin-key`

- Run by the tool [[confluence_get_admin_key]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/admin-key
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns information about the admin key if one is currently enabled for the calling user within the site.

**[Permissions](https://support.atlassian.com/user-management/docs/give-users-admin-permissions/#Centralized-user-management-content) required**:
User must be an organization or site admin.
