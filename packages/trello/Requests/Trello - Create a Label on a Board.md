---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/boards/{id}/labels"
category: "Boards"
writes_data: true
---
# Trello - Create a Label on a Board

**Create a Label on a Board** — `POST /boards/{id}/labels`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a Label on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/boards/{{param:id}}/labels?name={{param:name}}&color={{param:color}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The id of the board to update
- `name` (query, string, required) — The name of the label to be created. 1 to 16384 characters long.
- `color` (query, string, required) — Sets the color of the new label. Valid values are a label color or null.

## Original description

Create a new Label on a Board.
