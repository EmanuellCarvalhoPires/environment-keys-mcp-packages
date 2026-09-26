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
path: "/boards/{boardId}/boardStars"
category: "Boards"
writes_data: false
---
# Trello - Get boardStars on a Board

**Get boardStars on a Board** — `GET /boards/{boardId}/boardStars`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get boardStars on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:boardId}}/boardStars?filter={{param:filter}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `boardId` (path, string, required) — Value of boardId in the path.
- `filter` (query, string, optional) — Valid values: mine, none

