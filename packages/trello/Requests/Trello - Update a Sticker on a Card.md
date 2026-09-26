---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/cards/{id}/stickers/{idSticker}"
category: "Cards"
writes_data: true
---
# Trello - Update a Sticker on a Card

**Update a Sticker on a Card** — `PUT /cards/{id}/stickers/{idSticker}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a Sticker on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/cards/{{param:id}}/stickers/{{param:idSticker}}?top={{param:top}}&left={{param:left}}&zIndex={{param:zIndex}}&rotate={{param:rotate}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idSticker` (path, string, required) — Value of idSticker in the path.
- `top` (query, string, required) — The top position of the sticker, from -60 to 100
- `left` (query, string, required) — The left position of the sticker, from -60 to 100
- `zIndex` (query, string, required) — The z-index of the sticker
- `rotate` (query, string, optional) — The rotation of the sticker

## Original description

Update a sticker on a card
