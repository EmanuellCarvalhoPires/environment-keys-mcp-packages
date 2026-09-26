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
path: "/cards/{idCard}/customFields"
category: "Cards"
writes_data: true
---
# Trello - Update Multiple Custom Field items on Card

**Update Multiple Custom Field items on Card** — `PUT /cards/{idCard}/customFields`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update Multiple Custom Field items on Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/cards/{{param:idCard}}/customFields
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `idCard` (path, string, required) — Value of idCard in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Setting, updating, and removing the values for multiple Custom Fields on a card. For more details on updating custom fields check out the [Getting Started With Custom Fields](/cloud/trello/guides/rest-api/getting-started-with-custom-fields/)
