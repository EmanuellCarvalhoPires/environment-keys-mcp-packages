---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/members/{id}/boardStars/{idStar}"
category: "Members"
writes_data: false
---
# Trello - Get a boardStar of Member

**Get a boardStar of Member** — `GET /members/{id}/boardStars/{idStar}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a boardStar of Member"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/boardStars/{{param:idStar}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idStar` (path, string, required) — Value of idStar in the path.

## Original description

Get a specific boardStar
