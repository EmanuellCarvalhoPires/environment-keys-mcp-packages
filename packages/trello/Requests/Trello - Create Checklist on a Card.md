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
path: "/cards/{id}/checklists"
category: "Cards"
writes_data: true
---
# Trello - Create Checklist on a Card

**Create Checklist on a Card** — `POST /cards/{id}/checklists`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create Checklist on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/cards/{{param:id}}/checklists?name={{param:name}}&idChecklistSource={{param:idChecklistSource}}&pos={{param:pos}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `name` (query, string, optional) — The name of the checklist
- `idChecklistSource` (query, string, optional) — The ID of a source checklist to copy into the new one
- `pos` (query, string, optional) — The position of the checklist on the card. One of: top, bottom, or a positive number.

## Original description

Create a new checklist on a card
