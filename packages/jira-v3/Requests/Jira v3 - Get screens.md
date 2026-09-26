---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screens
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/screens"
category: "Screens"
writes_data: false
tool_note: "[[jira_get_screens]]"
---
# Jira v3 - Get screens

**Get screens** — `GET /rest/api/3/screens`

- Run by the tool [[jira_get_screens]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/screens?startAt={{param:startAt}}&maxResults={{param:maxResults}}&id={{param:id}}&queryString={{param:queryString}}&scope={{param:scope}}&orderBy={{param:orderBy}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `id` (query, string, optional) — The list of screen IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001.
- `queryString` (query, string, optional) — String used to perform a case-insensitive partial match with screen name.
- `scope` (query, string, optional) — The scope filter string. To filter by multiple scope, provide an ampersand-separated list. For example, scope=GLOBAL&scope=PROJECT.
- `orderBy` (query, string, optional) — Order the results by a field: id Sorts by screen ID. name Sorts by screen name.

## Original description

Returns a [paginated](#pagination) list of all screens or those specified by one or more screen IDs.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
