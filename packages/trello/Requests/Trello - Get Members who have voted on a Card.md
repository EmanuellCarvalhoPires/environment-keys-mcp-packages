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
path: "/cards/{id}/membersVoted"
category: "Cards"
writes_data: false
---
# Trello - Get Members who have voted on a Card

**Get Members who have voted on a Card** — `GET /cards/{id}/membersVoted`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Members who have voted on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/cards/{{param:id}}/membersVoted?fields={{param:fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `fields` (query, string, optional) — all or a comma-separated list of member fields

## Original description

Get the members who have voted on a card
