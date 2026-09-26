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
path: "/rest/api/3/priorityscheme/priorities/available"
category: "Priority schemes"
writes_data: false
tool_note: "[[jira_get_available_priorities_by_priority_scheme]]"
---
# Jira v3 - Get available priorities by priority scheme

**Get available priorities by priority scheme** — `GET /rest/api/3/priorityscheme/priorities/available`

- Run by the tool [[jira_get_available_priorities_by_priority_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/priorityscheme/priorities/available?startAt={{param:startAt}}&maxResults={{param:maxResults}}&query={{param:query}}&schemeId={{param:schemeId}}&exclude={{param:exclude}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `query` (query, string, optional) — The string to query priorities on by name.
- `schemeId` (query, string, required) — The priority scheme ID.
- `exclude` (query, string, optional) — A list of priority IDs to exclude from the results.

## Original description

Returns a [paginated](#pagination) list of priorities available for adding to a priority scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
