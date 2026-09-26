---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/lists
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/lists/{id}/board"
category: "Lists"
writes_data: false
---
# Trello - Get the Board a List is on

**Get the Board a List is on** — `GET /lists/{id}/board`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get the Board a List is on"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/lists/{{param:id}}/board?fields={{param:fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the list
- `fields` (query, string, optional) — all or a comma-separated list of board fields

## Original description

Get the board a list is on
