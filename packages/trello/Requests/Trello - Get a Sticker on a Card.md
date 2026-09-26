---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/cards/{id}/stickers/{idSticker}"
category: "Cards"
writes_data: false
---
# Trello - Get a Sticker on a Card

**Get a Sticker on a Card** — `GET /cards/{id}/stickers/{idSticker}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Sticker on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/cards/{{param:id}}/stickers/{{param:idSticker}}?fields={{param:fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idSticker` (path, string, required) — Value of idSticker in the path.
- `fields` (query, string, optional) — all or a comma-separated list of sticker fields

## Original description

Get a specific sticker on a card
