---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-role-actors
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/role/{id}/actors"
category: "Project role actors"
writes_data: false
tool_note: "[[jira_get_default_actors_for_project_role]]"
---
# Jira v3 - Get default actors for project role

**Get default actors for project role** — `GET /rest/api/3/role/{id}/actors`

- Run by the tool [[jira_get_default_actors_for_project_role]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/role/{{param:id}}/actors
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the project role. Use Get all project roles to get a list of project role IDs.

## Original description

Returns the [default actors](#api-rest-api-3-resolution-get) for the project role.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
