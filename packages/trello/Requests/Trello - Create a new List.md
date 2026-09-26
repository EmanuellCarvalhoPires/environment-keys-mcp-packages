---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/lists
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/lists"
category: "Lists"
writes_data: true
---
# Trello - Create a new List

**Create a new List** — `POST /lists`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a new List"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/lists?name={{param:name}}&idBoard={{param:idBoard}}&idListSource={{param:idListSource}}&pos={{param:pos}}
Authorization: {{service.auth_token}}
```

## Parameters

- `name` (query, string, required) — Name for the list
- `idBoard` (query, string, required) — The long ID of the board the list should be created on
- `idListSource` (query, string, optional) — ID of the List to copy into the new List
- `pos` (query, string, optional) — Position of the list. top, bottom, or a positive floating point number

## Original description

Create a new List on a Board
