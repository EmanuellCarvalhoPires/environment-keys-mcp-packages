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
path: "/boards/{id}/members"
category: "Boards"
writes_data: false
---
# Trello - Get the Members of a Board

**Get the Members of a Board** — `GET /boards/{id}/members`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get the Members of a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}/members
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Get the Members for a board
