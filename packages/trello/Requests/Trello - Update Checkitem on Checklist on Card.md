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
path: "/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}"
category: "Cards"
writes_data: true
---
# Trello - Update Checkitem on Checklist on Card

**Update Checkitem on Checklist on Card** — `PUT /cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update Checkitem on Checklist on Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/cards/{{param:idCard}}/checklist/{{param:idChecklist}}/checkItem/{{param:idCheckItem}}?pos={{param:pos}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `idCard` (path, string, required) — The ID of the Card
- `idChecklist` (path, string, required) — The ID of the item to update.
- `idCheckItem` (path, string, required) — The ID of the checklist item to update
- `pos` (query, string, optional) — top, bottom, or a positive float

## Original description

Update an item in a checklist on a card.
