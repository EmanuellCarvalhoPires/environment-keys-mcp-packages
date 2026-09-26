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
path: "/boards/{id}/labels"
category: "Boards"
writes_data: false
---
# Trello - Get Labels on a Board

**Get Labels on a Board** — `GET /boards/{id}/labels`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Labels on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}/labels?fields={{param:fields}}&limit={{param:limit}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Board.
- `fields` (query, string, optional) — The fields to be returned for the Labels.
- `limit` (query, string, optional) — The number of Labels to be returned.

## Original description

Get all of the Labels on a Board.
