---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/search"
category: "Projects"
writes_data: false
tool_note: "[[jira_get_projects_paginated]]"
---
# Jira v3 - Get projects paginated

**Get projects paginated** — `GET /rest/api/3/project/search`

- Run by the tool [[jira_get_projects_paginated]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/search?startAt={{param:startAt}}&maxResults={{param:maxResults}}&orderBy={{param:orderBy}}&id={{param:id}}&keys={{param:keys}}&query={{param:query}}&typeKey={{param:typeKey}}&categoryId={{param:categoryId}}&action={{param:action}}&expand={{param:expand}}&status={{param:status}}&properties={{param:properties}}&propertyQuery={{param:propertyQuery}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page. Must be less than or equal to 100. If a value greater than 100 is provided, the maxResults parameter will default to 100.
- `orderBy` (query, string, optional) — Order the results by a field. category Sorts by project category. A complete list of category IDs is found using Get all project categories.
- `id` (query, string, optional) — The project IDs to filter the results by. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001. Up to 50 project IDs can be provided.
- `keys` (query, string, optional) — The project keys to filter the results by. To include multiple keys, provide an ampersand-separated list. For example, keys=PA&keys=PB. Up to 50 project keys can be provided.
- `query` (query, string, optional) — Filter the results using a literal string. Projects with a matching key or name are returned (case insensitive).
- `typeKey` (query, string, optional) — Orders results by the project type. This parameter accepts a comma-separated list. Valid values are business, servicedesk, and software.
- `categoryId` (query, string, optional) — The ID of the project's category. A complete list of category IDs is found using the Get all project categories operation.
- `action` (query, string, optional) — Filter results by projects for which the user can: view the project, meaning that they have one of the following permissions: Browse projects project permission for the project.
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expanded options include: description Returns the project description.
- `status` (query, string, optional) — EXPERIMENTAL. Filter results by project status: live Search live projects. archived Search archived projects. deleted Search deleted projects, those in the recycle bin.
- `properties` (query, string, optional) — EXPERIMENTAL. A list of project properties to return for the project. This parameter accepts a comma-separated list.
- `propertyQuery` (query, string, optional) — EXPERIMENTAL. A query string used to search properties. The query string cannot be specified using a JSON object.

## Original description

Returns a [paginated](#pagination) list of projects visible to the user.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** Projects are returned only where the user has one of:

 *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
