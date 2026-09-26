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
path: "/rest/api/3/issuesecurityschemes/level/member"
category: "Issue security schemes"
writes_data: false
tool_note: "[[jira_get_issue_security_level_members]]"
---
# Jira v3 - Get issue security level members

**Get issue security level members** — `GET /rest/api/3/issuesecurityschemes/level/member`

- Run by the tool [[jira_get_issue_security_level_members]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuesecurityschemes/level/member?startAt={{param:startAt}}&maxResults={{param:maxResults}}&id={{param:id}}&schemeId={{param:schemeId}}&levelId={{param:levelId}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `id` (query, string, optional) — The list of issue security level member IDs. To include multiple issue security level members separate IDs with an ampersand: id=10000&id=10001.
- `schemeId` (query, string, optional) — The list of issue security scheme IDs. To include multiple issue security schemes separate IDs with an ampersand: schemeId=10000&schemeId=10001.
- `levelId` (query, string, optional) — The list of issue security level IDs. To include multiple issue security levels separate IDs with an ampersand: levelId=10000&levelId=10001.
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list.

## Original description

Returns a [paginated](#pagination) list of issue security level members.

Only issue security level members in the context of classic projects are returned.

Filtering using parameters is inclusive: if you specify both security scheme IDs and level IDs, the result will include all issue security level members from the specified schemes and levels.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
