---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/action
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/boards/{id}/boardPlugins"
category: "Boards"
writes_data: true
---
# Trello - Enable a Power-Up on a Board

**Enable a Power-Up on a Board** — `POST /boards/{id}/boardPlugins`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Enable a Power-Up on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/boards/{{param:id}}/boardPlugins?idPlugin={{param:idPlugin}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idPlugin` (query, string, optional) — The ID of the Power-Up to enable

## Original description

Enable a Power-Up on a Board
