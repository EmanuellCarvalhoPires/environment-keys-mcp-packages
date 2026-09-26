---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/cards/{id}/checkItem/{idCheckItem}"
category: "Cards"
writes_data: true
---
# Trello - Delete checkItem on a Card

**Delete checkItem on a Card** — `DELETE /cards/{id}/checkItem/{idCheckItem}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete checkItem on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/cards/{{param:id}}/checkItem/{{param:idCheckItem}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idCheckItem` (path, string, required) — Value of idCheckItem in the path.

## Original description

Delete a checklist item
