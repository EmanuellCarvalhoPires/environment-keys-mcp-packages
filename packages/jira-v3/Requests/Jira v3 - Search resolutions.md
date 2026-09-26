---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-resolutions
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/resolution/search"
category: "Issue resolutions"
writes_data: false
tool_note: "[[jira_search_resolutions]]"
---
# Jira v3 - Search resolutions

**Search resolutions** — `GET /rest/api/3/resolution/search`

- Run by the tool [[jira_search_resolutions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/resolution/search?startAt={{param:startAt}}&maxResults={{param:maxResults}}&id={{param:id}}&onlyDefault={{param:onlyDefault}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `id` (query, string, optional) — The list of resolutions IDs to be filtered out
- `onlyDefault` (query, string, optional) — When set to true, return default only, when IDs provided, if none of them is default, return empty page. Default value is false

## Original description

Returns a [paginated](#pagination) list of resolutions. The list can contain all resolutions or a subset determined by any combination of these criteria:

 *  a list of resolutions IDs.
 *  whether the field configuration is a default. This returns resolutions from company-managed (classic) projects only, as there is no concept of default resolutions in team-managed projects.

**[Permissions](#permissions) required:** Permission to access Jira.
