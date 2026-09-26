---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-priorities
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/priority/search"
category: "Issue priorities"
writes_data: false
tool_note: "[[jira_search_priorities]]"
---
# Jira v3 - Search priorities

**Search priorities** — `GET /rest/api/3/priority/search`

- Run by the tool [[jira_search_priorities]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/priority/search?startAt={{param:startAt}}&maxResults={{param:maxResults}}&id={{param:id}}&projectId={{param:projectId}}&priorityName={{param:priorityName}}&onlyDefault={{param:onlyDefault}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `id` (query, string, optional) — The list of priority IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=2&id=3.
- `projectId` (query, string, optional) — The list of projects IDs. To include multiple IDs, provide an ampersand-separated list. For example, projectId=10010&projectId=10111.
- `priorityName` (query, string, optional) — The name of priority to search for.
- `onlyDefault` (query, string, optional) — Whether only the default priority is returned.
- `expand` (query, string, optional) — Use schemes to return the associated priority schemes for each priority. Limited to returning first 15 priority schemes per priority.

## Original description

Returns a [paginated](#pagination) list of priorities. The list can contain all priorities or a subset determined by any combination of these criteria:

 *  a list of priority IDs. Any invalid priority IDs are ignored.
 *  a list of project IDs. Only priorities that are available in these projects will be returned. Any invalid project IDs are ignored.
 *  whether the field configuration is a default. This returns priorities from company-managed (classic) projects only, as there is no concept of default priorities in team-managed projects.

**Deprecation notice:** The `onlyDefault` parameter is deprecated and will be removed at a later date. See [CHANGE-1655](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-1655).

**Deprecation notice:** The `isDefault` property of priorities is deprecated and will be removed at a later date. See [CHANGE-1655](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-1655).

**[Permissions](#permissions) required:** Permission to access Jira.
