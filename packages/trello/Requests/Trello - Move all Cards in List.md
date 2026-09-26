---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/lists
  - api/operation/action
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/lists/{id}/moveAllCards"
category: "Lists"
writes_data: true
---
# Trello - Move all Cards in List

**Move all Cards in List** — `POST /lists/{id}/moveAllCards`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Move all Cards in List"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/lists/{{param:id}}/moveAllCards?idBoard={{param:idBoard}}&idList={{param:idList}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the list
- `idBoard` (query, string, required) — The ID of the board the cards should be moved to
- `idList` (query, string, required) — The ID of the list that the cards should be moved to

## Original description

Move all Cards in a List
