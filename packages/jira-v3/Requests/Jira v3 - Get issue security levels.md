---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issuesecurityschemes/level"
category: "Issue security schemes"
writes_data: false
tool_note: "[[jira_get_issue_security_levels]]"
---
# Jira v3 - Get issue security levels

**Get issue security levels** — `GET /rest/api/3/issuesecurityschemes/level`

- Run by the tool [[jira_get_issue_security_levels]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuesecurityschemes/level?startAt={{param:startAt}}&maxResults={{param:maxResults}}&id={{param:id}}&schemeId={{param:schemeId}}&onlyDefault={{param:onlyDefault}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `id` (query, string, optional) — The list of issue security scheme level IDs. To include multiple issue security levels, separate IDs with an ampersand: id=10000&id=10001.
- `schemeId` (query, string, optional) — The list of issue security scheme IDs. To include multiple issue security schemes, separate IDs with an ampersand: schemeId=10000&schemeId=10001.
- `onlyDefault` (query, string, optional) — When set to true, returns multiple default levels for each security scheme containing a default. If you provide scheme and level IDs not associated with the default, returns an empty page.

## Original description

Returns a [paginated](#pagination) list of issue security levels.

Only issue security levels in the context of classic projects are returned.

Filtering using IDs is inclusive: if you specify both security scheme IDs and level IDs, the result will include both specified issue security levels and all issue security levels from the specified schemes.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
