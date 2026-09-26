---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/boards/{id}/calendarKey/generate"
category: "Boards"
writes_data: true
---
# Trello - Create a calendarKey for a Board

**Create a calendarKey for a Board** — `POST /boards/{id}/calendarKey/generate`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a calendarKey for a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/boards/{{param:id}}/calendarKey/generate
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The id of the board to update

## Original description

Create a new board.
