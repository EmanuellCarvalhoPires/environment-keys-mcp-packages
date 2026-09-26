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
path: "/lists/{id}/actions"
category: "Lists"
writes_data: false
---
# Trello - Get Actions for a List

**Get Actions for a List** — `GET /lists/{id}/actions`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Actions for a List"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/lists/{{param:id}}/actions?filter={{param:filter}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the list
- `filter` (query, string, optional) — A comma-separated list of action types.

## Original description

Get the Actions on a List
