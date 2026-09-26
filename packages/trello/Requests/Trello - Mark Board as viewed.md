---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/action
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/boards/{id}/markAsViewed"
category: "Boards"
writes_data: true
---
# Trello - Mark Board as viewed

**Mark Board as viewed** — `POST /boards/{id}/markAsViewed`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Mark Board as viewed"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/boards/{{param:id}}/markAsViewed
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The id of the board to update

