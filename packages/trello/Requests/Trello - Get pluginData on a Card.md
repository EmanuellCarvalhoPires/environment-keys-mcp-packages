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
path: "/cards/{id}/pluginData"
category: "Cards"
writes_data: false
---
# Trello - Get pluginData on a Card

**Get pluginData on a Card** — `GET /cards/{id}/pluginData`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get pluginData on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/cards/{{param:id}}/pluginData
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Card

## Original description

Get any shared pluginData on a card.
