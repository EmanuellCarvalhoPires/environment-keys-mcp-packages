---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/boards/{id}/lists"
category: "Boards"
writes_data: false
---
# Trello - Get Lists on a Board

**Get Lists on a Board** — `GET /boards/{id}/lists`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Lists on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}/lists?cards={{param:cards}}&card_fields={{param:card_fields}}&filter={{param:filter}}&fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `cards` (query, string, optional) — Filter to apply to Cards.
- `card_fields` (query, string, optional) — all or a comma-separated list of card fields
- `filter` (query, string, optional) — Filter to apply to Lists
- `fields` (query, string, optional) — all or a comma-separated list of list fields

## Original description

Get the Lists on a Board
