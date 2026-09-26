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
path: "/cards/{id}/checklists"
category: "Cards"
writes_data: false
---
# Trello - Get Checklists on a Card

**Get Checklists on a Card** — `GET /cards/{id}/checklists`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Checklists on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/cards/{{param:id}}/checklists?checkItems={{param:checkItems}}&checkItem_fields={{param:checkItem_fields}}&filter={{param:filter}}&fields={{param:fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `checkItems` (query, string, optional) — all or none
- `checkItem_fields` (query, string, optional) — all or a comma-separated list of: name,nameData,pos,state,type,due,dueReminder,idMember
- `filter` (query, string, optional) — all or none
- `fields` (query, string, optional) — all or a comma-separated list of: idBoard,idCard,name,pos

## Original description

Get the checklists on a card
