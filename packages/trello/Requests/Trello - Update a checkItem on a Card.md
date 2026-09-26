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
path: "/cards/{id}/checkItem/{idCheckItem}"
category: "Cards"
writes_data: true
---
# Trello - Update a checkItem on a Card

**Update a checkItem on a Card** — `PUT /cards/{id}/checkItem/{idCheckItem}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a checkItem on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/cards/{{param:id}}/checkItem/{{param:idCheckItem}}?name={{param:name}}&state={{param:state}}&idChecklist={{param:idChecklist}}&pos={{param:pos}}&due={{param:due}}&dueReminder={{param:dueReminder}}&idMember={{param:idMember}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idCheckItem` (path, string, required) — Value of idCheckItem in the path.
- `name` (query, string, optional) — The new name for the checklist item
- `state` (query, string, optional) — One of: complete, incomplete
- `idChecklist` (query, string, optional) — The ID of the checklist this item is in
- `pos` (query, string, optional) — top, bottom, or a positive float
- `due` (query, string, optional) — A due date for the checkitem
- `dueReminder` (query, string, optional) — A dueReminder for the due date on the checkitem
- `idMember` (query, string, optional) — The ID of the member to remove from the card

## Original description

Update an item in a checklist on a card.
