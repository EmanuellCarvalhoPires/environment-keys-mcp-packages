---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/list
  - api/effect/read
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project"
category: "Projects"
writes_data: false
tool_note: "[[jira_get_all_projects]]"
---
# Jira v3 - Get all projects

**Get all projects** — `GET /rest/api/3/project`

- Run by the tool [[jira_get_all_projects]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project?expand={{param:expand}}&recent={{param:recent}}&properties={{param:properties}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include: description Returns the project description.
- `recent` (query, string, optional) — Returns the user's most recently accessed projects. You may specify the number of results to return up to a maximum of 20.
- `properties` (query, string, optional) — A list of project properties to return for the project. This parameter accepts a comma-separated list.

## Original description

Returns all projects visible to the user. Deprecated, use [ Get projects paginated](#api-rest-api-3-project-search-get) that supports search and pagination.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Projects are returned only where the user has *Browse Projects* or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
