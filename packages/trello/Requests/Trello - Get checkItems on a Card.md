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
path: "/cards/{id}/checkItemStates"
category: "Cards"
writes_data: false
---
# Trello - Get checkItems on a Card

**Get checkItems on a Card** — `GET /cards/{id}/checkItemStates`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get checkItems on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/cards/{{param:id}}/checkItemStates?fields={{param:fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `fields` (query, string, optional) — all or a comma-separated list of: idCheckItem, state

## Original description

Get the completed checklist items on a card
