---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/cards/{id}/idMembers/{idMember}"
category: "Cards"
writes_data: true
---
# Trello - Remove a Member from a Card

**Remove a Member from a Card** — `DELETE /cards/{id}/idMembers/{idMember}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Remove a Member from a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/cards/{{param:id}}/idMembers/{{param:idMember}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `idMember` (path, string, required) — The ID of the member to remove from the card

## Original description

Remove a member from a card
