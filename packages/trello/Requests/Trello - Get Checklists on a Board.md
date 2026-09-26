---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/boards/{id}/checklists"
category: "Boards"
writes_data: false
---
# Trello - Get Checklists on a Board

**Get Checklists on a Board** — `GET /boards/{id}/checklists`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Checklists on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}/checklists
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the board

## Original description

Get all of the checklists on a Board.
