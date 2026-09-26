---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/members/{id}/savedSearches/{idSearch}"
category: "Members"
writes_data: true
---
# Trello - Update a saved search

**Update a saved search** — `PUT /members/{id}/savedSearches/{idSearch}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a saved search"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/members/{{param:id}}/savedSearches/{{param:idSearch}}?name={{param:name}}&query={{param:query}}&pos={{param:pos}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idSearch` (path, string, required) — Value of idSearch in the path.
- `name` (query, string, optional) — The new name for the saved search
- `query` (query, string, optional) — The new search query
- `pos` (query, string, optional) — New position for saves search. top, bottom, or a positive float.

## Original description

Update a saved search
