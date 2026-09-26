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
path: "/boards/{id}/boardPlugins/{idPlugin}"
category: "Boards"
writes_data: true
---
# Trello - Disable a Power-Up on a Board

**Disable a Power-Up on a Board** — `DELETE /boards/{id}/boardPlugins/{idPlugin}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Disable a Power-Up on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/boards/{{param:id}}/boardPlugins/{{param:idPlugin}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the board
- `idPlugin` (path, string, required) — The ID of the Power-Up to disable

## Original description

Disable a Power-Up on a board
