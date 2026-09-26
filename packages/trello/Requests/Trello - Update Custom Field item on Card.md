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
path: "/cards/{idCard}/customField/{idCustomField}/item"
category: "Cards"
writes_data: true
---
# Trello - Update Custom Field item on Card

**Update Custom Field item on Card** — `PUT /cards/{idCard}/customField/{idCustomField}/item`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update Custom Field item on Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/cards/{{param:idCard}}/customField/{{param:idCustomField}}/item
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `idCard` (path, string, required) — ID of the card that the Custom Field value should be set/updated for
- `idCustomField` (path, string, required) — ID of the Custom Field on the card.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Setting, updating, and removing the value for a Custom Field on a card. For more details on updating custom fields check out the [Getting Started With Custom Fields](/cloud/trello/guides/rest-api/getting-started-with-custom-fields/)
