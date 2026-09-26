---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-roles
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectIdOrKey}/role"
category: "Project roles"
writes_data: false
tool_note: "[[jira_get_project_roles_for_project]]"
---
# Jira v3 - Get project roles for project

**Get project roles for project** — `GET /rest/api/3/project/{projectIdOrKey}/role`

- Run by the tool [[jira_get_project_roles_for_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/role
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).

## Original description

Returns a list of [project roles](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/) for the project returning the name and self URL for each role.

Note that all project roles are shared with all projects in Jira Cloud. See [Get all project roles](#api-rest-api-3-role-get) for more information.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for any project on the site or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
