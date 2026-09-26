---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/status
  - api/operation/search
  - api/effect/read
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/statuses/search"
category: "Status"
writes_data: false
tool_note: "[[jira_search_statuses_paginated]]"
---
# Jira v3 - Search statuses paginated

**Search statuses paginated** — `GET /rest/api/3/statuses/search`

- Run by the tool [[jira_search_statuses_paginated]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/statuses/search?projectId={{param:projectId}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}&searchString={{param:searchString}}&statusCategory={{param:statusCategory}}&includeGlobalStatuses={{param:includeGlobalStatuses}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectId` (query, string, optional) — The project the status is part of or null for global statuses.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `searchString` (query, string, optional) — Term to match status names against or null to search for all statuses in the search scope.
- `statusCategory` (query, string, optional) — Category of the status to filter by. The supported values are: TODO, INPROGRESS, and DONE.
- `includeGlobalStatuses` (query, string, optional) — Whether to include global statuses (scope = null, not tied to any project) in the response. Defaults to false. Only relevant for project scoped queries.

## Original description

Returns a [paginated](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#pagination) list of statuses that match a search on name or project.

**[Permissions](#permissions) required:**

 *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
 *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)
