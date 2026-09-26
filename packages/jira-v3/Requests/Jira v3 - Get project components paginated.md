---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-components
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectIdOrKey}/component"
category: "Project components"
writes_data: false
tool_note: "[[jira_get_project_components_paginated]]"
---
# Jira v3 - Get project components paginated

**Get project components paginated** — `GET /rest/api/3/project/{projectIdOrKey}/component`

- Run by the tool [[jira_get_project_components_paginated]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/component?startAt={{param:startAt}}&maxResults={{param:maxResults}}&orderBy={{param:orderBy}}&componentSource={{param:componentSource}}&query={{param:query}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `orderBy` (query, string, optional) — Order the results by a field: description Sorts by the component description. issueCount Sorts by the count of issues associated with the component.
- `componentSource` (query, string, optional) — The source of the components to return. Can be jira (default), compass or auto. When auto is specified, the API will return connected Compass components if the project is opted into Compass, otherwise…
- `query` (query, string, optional) — Filter the results using a literal string. Components with a matching name or description are returned (case insensitive).

## Original description

Returns a [paginated](#pagination) list of all components in a project. See the [Get project components](#api-rest-api-3-project-projectIdOrKey-components-get) resource if you want to get a full list of versions without pagination.

If your project uses Compass components, this API will return a list of Compass components that are linked to issues in that project.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
