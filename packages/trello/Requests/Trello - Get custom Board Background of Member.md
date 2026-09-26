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
path: "/members/{id}/customBoardBackgrounds/{idBackground}"
category: "Members"
writes_data: false
---
# Trello - Get custom Board Background of Member

**Get custom Board Background of Member** — `GET /members/{id}/customBoardBackgrounds/{idBackground}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get custom Board Background of Member"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/customBoardBackgrounds/{{param:idBackground}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idBackground` (path, string, required) — Value of idBackground in the path.

## Original description

Get a specific custom board background
