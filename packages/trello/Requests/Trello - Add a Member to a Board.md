---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/boards/{id}/members/{idMember}"
category: "Boards"
writes_data: true
---
# Trello - Add a Member to a Board

**Add a Member to a Board** — `PUT /boards/{id}/members/{idMember}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Add a Member to a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/boards/{{param:id}}/members/{{param:idMember}}?type={{param:type}}&allowBillableGuest={{param:allowBillableGuest}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idMember` (path, string, required) — Value of idMember in the path.
- `type` (query, string, required) — One of: admin, normal, observer. Determines the type of member this user will be on the board.
- `allowBillableGuest` (query, string, optional) — Optional param that allows organization admins to add multi-board guests onto a board.

## Original description

Add a member to the board.
