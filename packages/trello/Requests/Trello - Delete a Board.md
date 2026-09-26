---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/boards/{id}"
category: "Boards"
writes_data: true
---
# Trello - Delete a Board

**Delete a Board** — `DELETE /boards/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/boards/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The id of the board to delete

## Original description

Delete a board.
