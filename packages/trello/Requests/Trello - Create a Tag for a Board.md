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
path: "/boards/{id}/idTags"
category: "Boards"
writes_data: true
---
# Trello - Create a Tag for a Board

**Create a Tag for a Board** — `POST /boards/{id}/idTags`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a Tag for a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/boards/{{param:id}}/idTags?value={{param:value}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The id of the board to update
- `value` (query, string, required) — The id of a tag from the organization to which this board belongs.

