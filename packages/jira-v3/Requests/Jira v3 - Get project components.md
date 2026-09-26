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
path: "/rest/api/3/project/{projectIdOrKey}/components"
category: "Project components"
writes_data: false
tool_note: "[[jira_get_project_components]]"
---
# Jira v3 - Get project components

**Get project components** — `GET /rest/api/3/project/{projectIdOrKey}/components`

- Run by the tool [[jira_get_project_components]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/components?componentSource={{param:componentSource}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectIdOrKey` (path, string, required) — The project ID or project key (case sensitive).
- `componentSource` (query, string, optional) — The source of the components to return. Can be jira (default), compass or auto. When auto is specified, the API will return connected Compass components if the project is opted into Compass, otherwise…

## Original description

Returns all components in a project. See the [Get project components paginated](#api-rest-api-3-project-projectIdOrKey-component-get) resource if you want to get a full list of components with pagination.

If your project uses Compass components, this API will return a paginated list of Compass components that are linked to issues in that project.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
