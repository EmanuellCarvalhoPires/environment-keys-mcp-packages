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
path: "/cards/{id}/customFieldItems"
category: "Cards"
writes_data: false
---
# Trello - Get Custom Field Items for a Card

**Get Custom Field Items for a Card** — `GET /cards/{id}/customFieldItems`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Custom Field Items for a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/cards/{{param:id}}/customFieldItems
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the Card

## Original description

Get the custom field items for a card.
