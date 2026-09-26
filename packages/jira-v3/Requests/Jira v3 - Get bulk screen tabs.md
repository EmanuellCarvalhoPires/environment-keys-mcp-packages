---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/screen-tabs
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/screens/tabs"
category: "Screen tabs"
writes_data: false
tool_note: "[[jira_get_bulk_screen_tabs]]"
---
# Jira v3 - Get bulk screen tabs

**Get bulk screen tabs** — `GET /rest/api/3/screens/tabs`

- Run by the tool [[jira_get_bulk_screen_tabs]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/screens/tabs?screenId={{param:screenId}}&tabId={{param:tabId}}&startAt={{param:startAt}}&maxResult={{param:maxResult}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `screenId` (query, string, optional) — The list of screen IDs. To include multiple screen IDs, provide an ampersand-separated list. For example, screenId=10000&screenId=10001.
- `tabId` (query, string, optional) — The list of tab IDs. To include multiple tab IDs, provide an ampersand-separated list. For example, tabId=10000&tabId=10001.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResult` (query, string, optional) — The maximum number of items to return per page. The maximum number is 100,

## Original description

Returns the list of tabs for a bulk of screens.

**[Permissions](#permissions) required:**

 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
