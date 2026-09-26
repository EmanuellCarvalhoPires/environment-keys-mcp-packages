---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/cards/{id}/stickers"
category: "Cards"
writes_data: false
---
# Trello - Get Stickers on a Card

**Get Stickers on a Card** — `GET /cards/{id}/stickers`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Stickers on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/cards/{{param:id}}/stickers?fields={{param:fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `fields` (query, string, optional) — all or a comma-separated list of sticker fields

## Original description

Get the stickers on a card
