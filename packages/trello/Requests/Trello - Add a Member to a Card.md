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
path: "/cards/{id}/idMembers"
category: "Cards"
writes_data: true
---
# Trello - Add a Member to a Card

**Add a Member to a Card** — `POST /cards/{id}/idMembers`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Add a Member to a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/cards/{{param:id}}/idMembers?value={{param:value}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `value` (query, string, optional) — The ID of the Member to add to the card

## Original description

Add a member to a card
