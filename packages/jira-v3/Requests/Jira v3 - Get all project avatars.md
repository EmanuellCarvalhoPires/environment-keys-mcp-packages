---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-avatars
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectIdOrKey}/avatars"
category: "Project avatars"
writes_data: false
tool_note: "[[jira_get_all_project_avatars]]"
---
# Jira v3 - Get all project avatars

**Get all project avatars** — `GET /rest/api/3/project/{projectIdOrKey}/avatars`

- Run by the tool [[jira_get_all_project_avatars]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/avatars
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The ID or (case-sensitive) key of the project.

## Original description

Returns all project avatars, grouped by system and custom avatars.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
