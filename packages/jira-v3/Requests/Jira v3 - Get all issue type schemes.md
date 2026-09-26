---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issuetypescheme"
category: "Issue type schemes"
writes_data: false
tool_note: "[[jira_get_all_issue_type_schemes]]"
---
# Jira v3 - Get all issue type schemes

**Get all issue type schemes** — `GET /rest/api/3/issuetypescheme`

- Run by the tool [[jira_get_all_issue_type_schemes]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuetypescheme?startAt={{param:startAt}}&maxResults={{param:maxResults}}&id={{param:id}}&orderBy={{param:orderBy}}&expand={{param:expand}}&queryString={{param:queryString}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `id` (query, string, optional) — The list of issue type schemes IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001.
- `orderBy` (query, string, optional) — Order the results by a field: name Sorts by issue type scheme name. id Sorts by issue type scheme ID.
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list.
- `queryString` (query, string, optional) — String used to perform a case-insensitive partial match with issue type scheme name.

## Original description

Returns a [paginated](#pagination) list of issue type schemes.

Only issue type schemes used in classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
