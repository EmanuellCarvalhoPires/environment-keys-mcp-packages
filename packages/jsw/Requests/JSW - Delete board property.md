---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/board
  - api/operation/delete
  - api/effect/write
up: "[[MCP - JSW]]"
app: "JSW"
method: DELETE
path: "/rest/agile/1.0/board/{boardId}/properties/{propertyKey}"
category: "Board"
writes_data: true
tool_note: "[[jsw_delete_board_property]]"
---
# JSW - Delete board property

**Delete board property** — `DELETE /rest/agile/1.0/board/{boardId}/properties/{propertyKey}`

- Run by the tool [[jsw_delete_board_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/agile/1.0/board/{{param:boardId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `boardId` (path, string, required) — the id of the board from which the property will be removed.
- `propertyKey` (path, string, required) — the key of the property to remove.

## Original description

Removes the property from the board identified by the id. Ths user removing the property is required to have permissions to modify the board.
