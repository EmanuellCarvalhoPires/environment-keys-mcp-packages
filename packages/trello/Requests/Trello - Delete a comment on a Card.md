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
path: "/cards/{id}/actions/{idAction}/comments"
category: "Cards"
writes_data: true
---
# Trello - Delete a comment on a Card

**Delete a comment on a Card** — `DELETE /cards/{id}/actions/{idAction}/comments`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete a comment on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/cards/{{param:id}}/actions/{{param:idAction}}/comments
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idAction` (path, string, required) — Value of idAction in the path.

## Original description

Delete a comment
