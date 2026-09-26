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
path: "/rest/api/3/project/{projectIdOrKey}/version"
category: "Project versions"
writes_data: false
tool_note: "[[jira_get_project_versions_paginated]]"
---
# Jira v3 - Get project versions paginated

**Get project versions paginated** — `GET /rest/api/3/project/{projectIdOrKey}/version`

- Run by the tool [[jira_get_project_versions_paginated]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/version?startAt={{param:startAt}}&maxResults={{param:maxResults}}&orderBy={{param:orderBy}}&query={{param:query}}&status={{param:status}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `orderBy` (query, string, optional) — Order the results by a field: description Sorts by version description. name Sorts by version name. releaseDate Sorts by release date, starting with the oldest date.
- `query` (query, string, optional) — Filter the results using a literal string. Versions with matching name or description are returned (case insensitive).
- `status` (query, string, optional) — A list of status values used to filter the results by version status. This parameter accepts a comma-separated list. The status values are released, unreleased, and archived.
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list.

## Original description

Returns a [paginated](#pagination) list of all versions in a project. See the [Get project versions](#api-rest-api-3-project-projectIdOrKey-versions-get) resource if you want to get a full list of versions without pagination.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
