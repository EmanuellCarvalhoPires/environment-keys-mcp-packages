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
path: "/boards/{id}/lists"
category: "Boards"
writes_data: true
---
# Trello - Create a List on a Board

**Create a List on a Board** — `POST /boards/{id}/lists`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a List on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/boards/{{param:id}}/lists?name={{param:name}}&pos={{param:pos}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `name` (query, string, required) — The name of the list to be created. 1 to 16384 characters long.
- `pos` (query, string, optional) — Determines the position of the list. Valid values: top, bottom, or a positive number.

## Original description

Create a new List on a Board.
