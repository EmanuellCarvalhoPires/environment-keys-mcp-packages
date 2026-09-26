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
path: "/boards/{id}/customFields"
category: "Boards"
writes_data: false
---
# Trello - Get Custom Fields for Board

**Get Custom Fields for Board** — `GET /boards/{id}/customFields`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Custom Fields for Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}/customFields
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the board

## Original description

Get the Custom Field Definitions that exist on a board.
