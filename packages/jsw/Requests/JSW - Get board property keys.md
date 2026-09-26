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
path: "/rest/agile/1.0/board/{boardId}/properties"
category: "Board"
writes_data: false
tool_note: "[[jsw_get_board_property_keys]]"
---
# JSW - Get board property keys

**Get board property keys** — `GET /rest/agile/1.0/board/{boardId}/properties`

- Run by the tool [[jsw_get_board_property_keys]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/properties
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — the ID of the board from which property keys will be returned.

## Original description

Returns the keys of all properties for the board identified by the id. The user who retrieves the property keys is required to have permissions to view the board.
