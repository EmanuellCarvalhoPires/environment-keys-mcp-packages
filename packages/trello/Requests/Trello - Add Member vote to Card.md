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
path: "/cards/{id}/membersVoted"
category: "Cards"
writes_data: true
---
# Trello - Add Member vote to Card

**Add Member vote to Card** — `POST /cards/{id}/membersVoted`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Add Member vote to Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/cards/{{param:id}}/membersVoted?value={{param:value}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `value` (query, string, required) — The ID of the member to vote 'yes' on the card

## Original description

Vote on the card for a given member.
