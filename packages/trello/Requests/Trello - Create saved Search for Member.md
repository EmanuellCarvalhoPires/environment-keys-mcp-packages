---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/members/{id}/savedSearches"
category: "Members"
writes_data: true
---
# Trello - Create saved Search for Member

**Create saved Search for Member** — `POST /members/{id}/savedSearches`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create saved Search for Member"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/members/{{param:id}}/savedSearches?name={{param:name}}&query={{param:query}}&pos={{param:pos}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `name` (query, string, required) — The name for the saved search
- `query` (query, string, required) — The search query
- `pos` (query, string, required) — The position of the saved search. top, bottom, or a positive float.

## Original description

Create a saved search
