---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/members/{id}/boardStars/{idStar}"
category: "Members"
writes_data: true
---
# Trello - Delete Star for Board

**Delete Star for Board** — `DELETE /members/{id}/boardStars/{idStar}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete Star for Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/members/{{param:id}}/boardStars/{{param:idStar}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idStar` (path, string, required) — Value of idStar in the path.

## Original description

Unstar a board
