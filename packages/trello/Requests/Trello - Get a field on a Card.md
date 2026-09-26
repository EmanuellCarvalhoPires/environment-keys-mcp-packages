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
path: "/cards/{id}/{field}"
category: "Cards"
writes_data: false
---
# Trello - Get a field on a Card

**Get a field on a Card** — `GET /cards/{id}/{field}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a field on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/cards/{{param:id}}/{{param:field}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `field` (path, string, required) — The desired field.

## Original description

Get a specific property of a card
