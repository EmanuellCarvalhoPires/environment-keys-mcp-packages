---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/cards/{id}/checkItem/{idCheckItem}"
category: "Cards"
writes_data: false
---
# Trello - Get checkItem on a Card

**Get checkItem on a Card** — `GET /cards/{id}/checkItem/{idCheckItem}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get checkItem on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/cards/{{param:id}}/checkItem/{{param:idCheckItem}}?fields={{param:fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idCheckItem` (path, string, required) — Value of idCheckItem in the path.
- `fields` (query, string, optional) — all or a comma-separated list of name,nameData,pos,state,type,due,dueReminder,idMember

## Original description

Get a specific checkItem on a card
