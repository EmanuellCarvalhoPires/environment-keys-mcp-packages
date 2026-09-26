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
path: "/boards/{id}/cards"
category: "Boards"
writes_data: false
---
# Trello - Get Cards on a Board

**Get Cards on a Board** — `GET /boards/{id}/cards`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Cards on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}/cards
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Get all of the open Cards on a Board. See [Nested Resources](/cloud/trello/guides/rest-api/nested-resources/) for more information.
