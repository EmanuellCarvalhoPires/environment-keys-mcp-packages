---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/update
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: PUT
path: "/rest/agile/1.0/board/{boardId}/properties/{propertyKey}"
category: "Board"
writes_data: true
tool_note: "[[jsw_set_board_property]]"
---
# JSW - Set board property

**Set board property** — `PUT /rest/agile/1.0/board/{boardId}/properties/{propertyKey}`

- Run by the tool [[jsw_set_board_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
PUT {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `boardId` (path, string, required) — the ID of the board on which the property will be set.
- `propertyKey` (path, string, required) — the key of the board's property. The maximum length of the key is 255 bytes.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Sets the value of the specified board's property.

You can use this resource to store a custom data against the board identified by the id. The user who stores the data is required to have permissions to modify the board.
