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
path: "/rest/agile/1.0/board/{boardId}/epic"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_epics]]"
---
# JSW - Get epics

**Get epics** — `GET /rest/agile/1.0/board/{boardId}/epic`

- Run by the tool [[jsw_get_epics]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/epic?startAt={{param:startAt}}&maxResults={{param:maxResults}}&done={{param:done}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — The ID of the board that contains the requested epics.
- `startAt` (query, string, optional) — The starting index of the returned epics. Base index: 0. See the 'Pagination' section at the top of this page for more details.
- `maxResults` (query, string, optional) — The maximum number of epics to return per page. See the 'Pagination' section at the top of this page for more details.
- `done` (query, string, optional) — Filters results to epics that are either done or not done. Valid values: true, false.

## Original description

Returns all epics from the board, for the given board ID. This only includes epics that the user has permission to view. Note, if the user does not have permission to view the board, no epics will be returned at all.
