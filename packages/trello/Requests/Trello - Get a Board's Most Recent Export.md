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
path: "/boards/{id}/exports/mostRecent"
category: "Boards"
writes_data: false
---
# Trello - Get a Board's Most Recent Export

**Get a Board's Most Recent Export** — `GET /boards/{id}/exports/mostRecent`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Board's Most Recent Export"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}/exports/mostRecent
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Get the most recent successful export for a board
