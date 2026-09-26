---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/lists
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/lists/{id}"
category: "Lists"
writes_data: false
---
# Trello - Get a List

**Get a List** — `GET /lists/{id}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a List"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/lists/{{param:id}}?fields={{param:fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `fields` (query, string, optional) — all or a comma separated list of List field names.

## Original description

Get information about a List
