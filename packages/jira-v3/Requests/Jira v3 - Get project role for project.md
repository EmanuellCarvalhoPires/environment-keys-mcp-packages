---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-roles
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectIdOrKey}/role/{id}"
category: "Project roles"
writes_data: false
tool_note: "[[jira_get_project_role_for_project]]"
---
# Jira v3 - Get project role for project

**Get project role for project** — `GET /rest/api/3/project/{projectIdOrKey}/role/{id}`

- Run by the tool [[jira_get_project_role_for_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/role/{{param:id}}?excludeInactiveUsers={{param:excludeInactiveUsers}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).
- `id` (path, string, required) — The ID of the project role. Use Get all project roles to get a list of project role IDs.
- `excludeInactiveUsers` (query, string, optional) — Exclude inactive users.

## Original description

Returns a project role's details and actors associated with the project. The list of actors is sorted by display name.

To check whether a user belongs to a role based on their group memberships, use [Get user](#api-rest-api-3-user-get) with the `groups` expand parameter selected. Then check whether the user keys and groups match with the actors returned for the project.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
