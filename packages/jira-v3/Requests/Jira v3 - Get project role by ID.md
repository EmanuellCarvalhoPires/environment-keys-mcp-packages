---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-roles
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/role/{id}"
category: "Project roles"
writes_data: false
tool_note: "[[jira_get_project_role_by_id]]"
---
# Jira v3 - Get project role by ID

**Get project role by ID** — `GET /rest/api/3/role/{id}`

- Run by the tool [[jira_get_project_role_by_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/role/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the project role. Use Get all project roles to get a list of project role IDs.

## Original description

Gets the project role details and the default actors associated with the role. The list of default actors is sorted by display name.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
