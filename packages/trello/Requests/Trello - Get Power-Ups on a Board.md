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
path: "/boards/{id}/plugins"
category: "Boards"
writes_data: false
---
# Trello - Get Power-Ups on a Board

**Get Power-Ups on a Board** — `GET /boards/{id}/plugins`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Power-Ups on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}/plugins?filter={{param:filter}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the board
- `filter` (query, string, optional) — One of: enabled or available

## Original description

List the Power-Ups on a board
