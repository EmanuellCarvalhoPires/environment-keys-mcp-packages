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
path: "/rest/agile/1.0/board/{boardId}/sprint"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_all_sprints]]"
---
# JSW - Get all sprints

**Get all sprints** — `GET /rest/agile/1.0/board/{boardId}/sprint`

- Run by the tool [[jsw_get_all_sprints]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/sprint?startAt={{param:startAt}}&maxResults={{param:maxResults}}&state={{param:state}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — The ID of the board that contains the requested sprints.
- `startAt` (query, string, optional) — The starting index of the returned sprints. Base index: 0. See the 'Pagination' section at the top of this page for more details.
- `maxResults` (query, string, optional) — The maximum number of sprints to return per page. See the 'Pagination' section at the top of this page for more details.
- `state` (query, string, optional) — Filters results to sprints in specified states. Valid values: future, active, closed. You can define multiple states separated by commas, e.g. state=active,closed

## Original description

Returns all sprints from a board, for a given board ID. This only includes sprints that the user has permission to view.
