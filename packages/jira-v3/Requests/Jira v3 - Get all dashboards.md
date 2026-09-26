---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/dashboards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/dashboard"
category: "Dashboards"
writes_data: false
tool_note: "[[jira_get_all_dashboards]]"
---
# Jira v3 - Get all dashboards

**Get all dashboards** — `GET /rest/api/3/dashboard`

- Run by the tool [[jira_get_all_dashboards]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/dashboard?filter={{param:filter}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `filter` (query, string, optional) — The filter applied to the list of dashboards. Valid values are: favourite Returns dashboards the user has marked as favorite. my Returns dashboards owned by the user.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a list of dashboards owned by or shared with the user. The list may be filtered to include only favorite or owned dashboards.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
