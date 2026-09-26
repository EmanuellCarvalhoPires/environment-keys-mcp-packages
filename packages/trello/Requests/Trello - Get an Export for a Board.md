---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/boards/{id}/exports/{idExport}"
category: "Boards"
writes_data: false
---
# Trello - Get an Export for a Board

**Get an Export for a Board** — `GET /boards/{id}/exports/{idExport}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get an Export for a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}/exports/{{param:idExport}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idExport` (path, string, required) — Value of idExport in the path.

## Original description

Get the status of a board export
