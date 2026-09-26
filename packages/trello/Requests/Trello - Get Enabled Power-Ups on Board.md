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
path: "/boards/{id}/boardPlugins"
category: "Boards"
writes_data: false
---
# Trello - Get Enabled Power-Ups on Board

**Get Enabled Power-Ups on Board** — `GET /boards/{id}/boardPlugins`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Enabled Power-Ups on Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}/boardPlugins
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Get the enabled Power-Ups on a board
