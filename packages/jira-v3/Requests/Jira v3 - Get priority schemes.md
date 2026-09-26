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
path: "/rest/api/3/priorityscheme"
category: "Priority schemes"
writes_data: false
tool_note: "[[jira_get_priority_schemes]]"
---
# Jira v3 - Get priority schemes

**Get priority schemes** — `GET /rest/api/3/priorityscheme`

- Run by the tool [[jira_get_priority_schemes]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/priorityscheme?startAt={{param:startAt}}&maxResults={{param:maxResults}}&priorityId={{param:priorityId}}&schemeId={{param:schemeId}}&schemeName={{param:schemeName}}&onlyDefault={{param:onlyDefault}}&orderBy={{param:orderBy}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `priorityId` (query, string, optional) — A set of priority IDs to filter by. To include multiple IDs, provide an ampersand-separated list. For example, priorityId=10000&priorityId=10001.
- `schemeId` (query, string, optional) — A set of priority scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, schemeId=10000&schemeId=10001.
- `schemeName` (query, string, optional) — The name of scheme to search for.
- `onlyDefault` (query, string, optional) — Whether only the default priority is returned.
- `orderBy` (query, string, optional) — The ordering to return the priority schemes by.
- `expand` (query, string, optional) — A comma separated list of additional information to return. "priorities" will return priorities associated with the priority scheme.

## Original description

Returns a [paginated](#pagination) list of priority schemes.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
