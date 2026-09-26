---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/priority-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/priorityscheme/{schemeId}/projects"
category: "Priority schemes"
writes_data: false
tool_note: "[[jira_get_projects_by_priority_scheme]]"
---
# Jira v3 - Get projects by priority scheme

**Get projects by priority scheme** — `GET /rest/api/3/priorityscheme/{schemeId}/projects`

- Run by the tool [[jira_get_projects_by_priority_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/priorityscheme/{{param:schemeId}}/projects?startAt={{param:startAt}}&maxResults={{param:maxResults}}&projectId={{param:projectId}}&query={{param:query}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `schemeId` (path, string, required) — The priority scheme ID.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `projectId` (query, string, optional) — The project IDs to filter by. For example, projectId=10000&projectId=10001.
- `query` (query, string, optional) — The string to query projects on by name.

## Original description

Returns a [paginated](#pagination) list of projects by scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
