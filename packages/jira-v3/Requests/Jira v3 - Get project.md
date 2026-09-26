---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectIdOrKey}"
category: "Projects"
writes_data: false
tool_note: "[[jira_get_project]]"
---
# Jira v3 - Get project

**Get project** — `GET /rest/api/3/project/{projectIdOrKey}`

- Run by the tool [[jira_get_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}?expand={{param:expand}}&properties={{param:properties}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list.
- `properties` (query, string, optional) — A list of project properties to return for the project. This parameter accepts a comma-separated list.

## Original description

Returns the [project details](https://confluence.atlassian.com/x/ahLpNw) for a project.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
