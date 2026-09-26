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
path: "/cards/{id}/stickers/{idSticker}"
category: "Cards"
writes_data: true
---
# Trello - Delete a Sticker on a Card

**Delete a Sticker on a Card** — `DELETE /cards/{id}/stickers/{idSticker}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete a Sticker on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/cards/{{param:id}}/stickers/{{param:idSticker}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idSticker` (path, string, required) — Value of idSticker in the path.

## Original description

Remove a sticker from the card
