---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/screenscheme"
category: "Screen schemes"
writes_data: false
tool_note: "[[jira_get_screen_schemes]]"
---
# Jira v3 - Get screen schemes

**Get screen schemes** — `GET /rest/api/3/screenscheme`

- Run by the tool [[jira_get_screen_schemes]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/screenscheme?startAt={{param:startAt}}&maxResults={{param:maxResults}}&id={{param:id}}&expand={{param:expand}}&queryString={{param:queryString}}&orderBy={{param:orderBy}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `id` (query, string, optional) — The list of screen scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001.
- `expand` (query, string, optional) — Use expand include additional information in the response. This parameter accepts issueTypeScreenSchemes that, for each screen schemes, returns information about the issue type screen scheme the scree…
- `queryString` (query, string, optional) — String used to perform a case-insensitive partial match with screen scheme name.
- `orderBy` (query, string, optional) — Order the results by a field: id Sorts by screen scheme ID. name Sorts by screen scheme name.

## Original description

Returns a [paginated](#pagination) list of screen schemes.

Only screen schemes used in classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
