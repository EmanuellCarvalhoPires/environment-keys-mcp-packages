---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-notification-schemes
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/notificationscheme/project"
category: "Issue notification schemes"
writes_data: false
tool_note: "[[jira_get_projects_using_notification_schemes_paginated]]"
---
# Jira v3 - Get projects using notification schemes paginated

**Get projects using notification schemes paginated** — `GET /rest/api/3/notificationscheme/project`

- Run by the tool [[jira_get_projects_using_notification_schemes_paginated]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/notificationscheme/project?startAt={{param:startAt}}&maxResults={{param:maxResults}}&notificationSchemeId={{param:notificationSchemeId}}&projectId={{param:projectId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `notificationSchemeId` (query, string, optional) — The list of notifications scheme IDs to be filtered out
- `projectId` (query, string, optional) — The list of project IDs to be filtered out

## Original description

Returns a [paginated](#pagination) mapping of project that have notification scheme assigned. You can provide either one or multiple notification scheme IDs or project IDs to filter by. If you don't provide any, this will return a list of all mappings. Note that only company-managed (classic) projects are supported. This is because team-managed projects don't have a concept of a default notification scheme. The mappings are ordered by projectId.

**[Permissions](#permissions) required:** Permission to access Jira.
