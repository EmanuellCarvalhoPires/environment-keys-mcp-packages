---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/boards/{id}/exports/{idExport}"
category: "Boards"
writes_data: true
---
# Trello - Delete an Export for a Board

**Delete an Export for a Board** — `DELETE /boards/{id}/exports/{idExport}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete an Export for a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/boards/{{param:id}}/exports/{{param:idExport}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idExport` (path, string, required) — Value of idExport in the path.

## Original description

Soft-delete a board export
