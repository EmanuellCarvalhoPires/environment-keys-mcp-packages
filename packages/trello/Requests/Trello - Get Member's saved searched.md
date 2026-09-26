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
path: "/members/{id}/savedSearches"
category: "Members"
writes_data: false
---
# Trello - Get Member's saved searched

**Get Member's saved searched** — `GET /members/{id}/savedSearches`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Member's saved searched"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/savedSearches
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

List the saved searches of a Member
