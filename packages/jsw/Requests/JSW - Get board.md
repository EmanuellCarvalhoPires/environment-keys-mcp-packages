---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/agile/1.0/board/{boardId}"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_board]]"
---
# JSW - Get board

**Get board** — `GET /rest/agile/1.0/board/{boardId}`

- Run by the tool [[jsw_get_board]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board/{{param:boardId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — The ID of the requested board.

## Original description

Returns the board for the given board ID. This board will only be returned if the user has permission to view it. Admins without the view permission will see the board as a private one, so will see only a subset of the board's data (board location for instance).
