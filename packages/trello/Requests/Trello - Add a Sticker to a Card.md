---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/cards/{id}/stickers"
category: "Cards"
writes_data: true
---
# Trello - Add a Sticker to a Card

**Add a Sticker to a Card** — `POST /cards/{id}/stickers`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Add a Sticker to a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/cards/{{param:id}}/stickers?image={{param:image}}&top={{param:top}}&left={{param:left}}&zIndex={{param:zIndex}}&rotate={{param:rotate}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `image` (query, string, required) — For custom stickers, the id of the sticker. For default stickers, the string identifier (like 'taco-cool', see below)
- `top` (query, string, required) — The top position of the sticker, from -60 to 100
- `left` (query, string, required) — The left position of the sticker, from -60 to 100
- `zIndex` (query, string, required) — The z-index of the sticker
- `rotate` (query, string, optional) — The rotation of the sticker

## Original description

Add a sticker to a card
