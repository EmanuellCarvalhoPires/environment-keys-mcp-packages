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
path: "/cards/{id}/membersVoted/{idMember}"
category: "Cards"
writes_data: true
---
# Trello - Remove a Member's Vote on a Card

**Remove a Member's Vote on a Card** — `DELETE /cards/{id}/membersVoted/{idMember}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Remove a Member's Vote on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/cards/{{param:id}}/membersVoted/{{param:idMember}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `idMember` (path, string, required) — The ID of the member whose vote to remove

## Original description

Remove a member's vote from a card
