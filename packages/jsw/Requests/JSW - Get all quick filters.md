---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/agile/1.0/board/{boardId}/quickfilter"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_all_quick_filters]]"
---
# JSW - Get all quick filters

**Get all quick filters** — `GET /rest/agile/1.0/board/{boardId}/quickfilter`

- Run by the tool [[jsw_get_all_quick_filters]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/quickfilter?startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — The ID of the board that contains the requested quick filters.
- `startAt` (query, string, optional) — The starting index of the returned quick filters. Base index: 0. See the 'Pagination' section at the top of this page for more details.
- `maxResults` (query, string, optional) — The maximum number of sprints to return per page. See the 'Pagination' section at the top of this page for more details.

## Original description

Returns all quick filters from a board, for a given board ID.
