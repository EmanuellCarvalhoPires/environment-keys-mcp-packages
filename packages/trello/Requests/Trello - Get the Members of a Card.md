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
path: "/cards/{id}/members"
category: "Cards"
writes_data: false
---
# Trello - Get the Members of a Card

**Get the Members of a Card** — `GET /cards/{id}/members`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get the Members of a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/cards/{{param:id}}/members?fields={{param:fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `fields` (query, string, optional) — all or a comma-separated list of member fields

## Original description

Get the members on a card
