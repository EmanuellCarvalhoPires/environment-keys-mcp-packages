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
path: "/boards/{id}/members/{idMember}"
category: "Boards"
writes_data: true
---
# Trello - Remove Member from Board

**Remove Member from Board** — `DELETE /boards/{id}/members/{idMember}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Remove Member from Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/boards/{{param:id}}/members/{{param:idMember}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idMember` (path, string, required) — Value of idMember in the path.

