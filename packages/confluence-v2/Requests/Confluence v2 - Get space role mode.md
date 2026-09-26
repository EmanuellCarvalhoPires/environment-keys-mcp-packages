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
path: "/space-role-mode"
category: "Space Roles"
writes_data: false
tool_note: "[[confluence_get_space_role_mode]]"
---
# Confluence v2 - Get space role mode

**Get space role mode** — `GET /space-role-mode`

- Run by the tool [[confluence_get_space_role_mode]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/space-role-mode
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Retrieves the space role mode.

Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
