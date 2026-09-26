---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-versions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectIdOrKey}/versions"
category: "Project versions"
writes_data: false
tool_note: "[[jira_get_project_versions]]"
---
# Jira v3 - Get project versions

**Get project versions** — `GET /rest/api/3/project/{projectIdOrKey}/versions`

- Run by the tool [[jira_get_project_versions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/versions?expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts operations, which returns actions that can be performed on the version.

## Original description

Returns all versions in a project. The response is not paginated. Use [Get project versions paginated](#api-rest-api-3-project-projectIdOrKey-version-get) if you want to get the versions in a project with pagination.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
