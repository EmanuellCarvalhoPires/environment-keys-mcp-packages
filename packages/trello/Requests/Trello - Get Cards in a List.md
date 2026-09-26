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
path: "/lists/{id}/cards"
category: "Lists"
writes_data: false
---
# Trello - Get Cards in a List

**Get Cards in a List** — `GET /lists/{id}/cards`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Cards in a List"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/lists/{{param:id}}/cards
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the list

## Original description

List the cards in a list
