---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/permissions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/permissions"
category: "Permissions"
writes_data: false
tool_note: "[[jira_get_all_permissions]]"
---
# Jira v3 - Get all permissions

**Get all permissions** — `GET /rest/api/3/permissions`

- Run by the tool [[jira_get_all_permissions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/permissions
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns all permissions, including:

 *  global permissions.
 *  project permissions.
 *  global permissions added by plugins.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
