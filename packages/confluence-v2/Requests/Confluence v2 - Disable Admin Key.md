---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/admin-key
  - api/operation/delete
  - api/effect/write
  - api/version/v2
  - api/permission/global-admin
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: DELETE
path: "/admin-key"
category: "Admin Key"
writes_data: true
tool_note: "[[confluence_disable_admin_key]]"
---
# Confluence v2 - Disable Admin Key

**Disable Admin Key** — `DELETE /admin-key`

- Run by the tool [[confluence_disable_admin_key]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
DELETE {{service.url}}/wiki/api/v2/admin-key
Authorization: {{service.auth_token}}
```

## Original description

Disables admin key access for the calling user within the site.

**[Permissions](https://support.atlassian.com/user-management/docs/give-users-admin-permissions/#Centralized-user-management-content) required**:
User must be an organization or site admin.
