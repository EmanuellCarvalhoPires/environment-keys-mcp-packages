---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/search
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/members/{id}/savedSearches/{idSearch}"
category: "Members"
writes_data: false
---
# Trello - Get a saved search

**Get a saved search** — `GET /members/{id}/savedSearches/{idSearch}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a saved search"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/savedSearches/{{param:idSearch}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idSearch` (path, string, required) — Value of idSearch in the path.

## Original description

Get a saved search
