---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/lists
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/lists/{id}/idBoard"
category: "Lists"
writes_data: true
---
# Trello - Move List to Board

**Move List to Board** — `PUT /lists/{id}/idBoard`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Move List to Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/lists/{{param:id}}/idBoard?value={{param:value}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the list
- `value` (query, string, required) — The ID of the board to move the list to

## Original description

Move a List to a different Board
