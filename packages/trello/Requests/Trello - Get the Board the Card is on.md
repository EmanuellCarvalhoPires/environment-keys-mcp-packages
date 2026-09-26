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
path: "/cards/{id}/board"
category: "Cards"
writes_data: false
---
# Trello - Get the Board the Card is on

**Get the Board the Card is on** — `GET /cards/{id}/board`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get the Board the Card is on"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/cards/{{param:id}}/board?fields={{param:fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `fields` (query, string, optional) — all or a comma-separated list of board fields

## Original description

Get the board a card is on
