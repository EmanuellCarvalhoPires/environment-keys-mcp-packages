---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/members/{id}/savedSearches/{idSearch}"
category: "Members"
writes_data: true
---
# Trello - Delete a saved search

**Delete a saved search** — `DELETE /members/{id}/savedSearches/{idSearch}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete a saved search"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/members/{{param:id}}/savedSearches/{{param:idSearch}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idSearch` (path, string, required) — Value of idSearch in the path.

## Original description

Delete a saved search
