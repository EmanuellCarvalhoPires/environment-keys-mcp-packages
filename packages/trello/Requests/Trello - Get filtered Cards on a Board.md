---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/boards/{id}/cards/{filter}"
category: "Boards"
writes_data: false
---
# Trello - Get filtered Cards on a Board

**Get filtered Cards on a Board** — `GET /boards/{id}/cards/{filter}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get filtered Cards on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}/cards/{{param:filter}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — ID of the Board
- `filter` (path, string, required) — One of: all, closed, complete, incomplete, none, open, visible

## Original description

Get the Cards on a Board that match a given filter. See [Nested Resources](/cloud/trello/guides/rest-api/nested-resources/) for more information.
