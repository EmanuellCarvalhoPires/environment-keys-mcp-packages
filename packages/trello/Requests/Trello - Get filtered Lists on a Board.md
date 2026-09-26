---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/boards/{id}/lists/{filter}"
category: "Boards"
writes_data: false
---
# Trello - Get filtered Lists on a Board

**Get filtered Lists on a Board** — `GET /boards/{id}/lists/{filter}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get filtered Lists on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}/lists/{{param:filter}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the board
- `filter` (path, string, required) — One of all, closed, none, open

