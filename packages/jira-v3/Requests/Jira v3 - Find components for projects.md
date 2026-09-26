---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-components
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/component"
category: "Project components"
writes_data: false
tool_note: "[[jira_find_components_for_projects]]"
---
# Jira v3 - Find components for projects

**Find components for projects** — `GET /rest/api/3/component`

- Run by the tool [[jira_find_components_for_projects]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/component?projectIdsOrKeys={{param:projectIdsOrKeys}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}&orderBy={{param:orderBy}}&query={{param:query}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdsOrKeys` (query, string, optional) — The project IDs and/or project keys (case sensitive).
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `orderBy` (query, string, optional) — Order the results by a field: description Sorts by the component description. name Sorts by component name.
- `query` (query, string, optional) — Filter the results using a literal string. Components with a matching name or description are returned (case insensitive).

## Original description

Returns a [paginated](#pagination) list of all components in a project, including global (Compass) components when applicable.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
