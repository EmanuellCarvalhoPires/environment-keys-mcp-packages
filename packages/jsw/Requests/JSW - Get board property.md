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
path: "/rest/agile/1.0/board/{boardId}/properties/{propertyKey}"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_board_property]]"
---
# JSW - Get board property

**Get board property** — `GET /rest/agile/1.0/board/{boardId}/properties/{propertyKey}`

- Run by the tool [[jsw_get_board_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — the ID of the board from which the property will be returned.
- `propertyKey` (path, string, required) — the key of the property to return.

## Original description

Returns the value of the property with a given key from the board identified by the provided id. The user who retrieves the property is required to have permissions to view the board.
