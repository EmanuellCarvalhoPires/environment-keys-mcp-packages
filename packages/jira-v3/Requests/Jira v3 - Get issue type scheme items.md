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
path: "/rest/api/3/issuetypescheme/mapping"
category: "Issue type schemes"
writes_data: false
tool_note: "[[jira_get_issue_type_scheme_items]]"
---
# Jira v3 - Get issue type scheme items

**Get issue type scheme items** — `GET /rest/api/3/issuetypescheme/mapping`

- Run by the tool [[jira_get_issue_type_scheme_items]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issuetypescheme/mapping?startAt={{param:startAt}}&maxResults={{param:maxResults}}&issueTypeSchemeId={{param:issueTypeSchemeId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `issueTypeSchemeId` (query, string, optional) — The list of issue type scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, issueTypeSchemeId=10000&issueTypeSchemeId=10001.

## Original description

Returns a [paginated](#pagination) list of issue type scheme items.

Only issue type scheme items used in classic projects are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
