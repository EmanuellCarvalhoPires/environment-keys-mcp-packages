---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/members/{id}/boardStars"
category: "Members"
writes_data: false
---
# Trello - Get a Member's boardStars

**Get a Member's boardStars** — `GET /members/{id}/boardStars`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Member's boardStars"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/boardStars
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID or username of the member

## Original description

List a member's board stars
