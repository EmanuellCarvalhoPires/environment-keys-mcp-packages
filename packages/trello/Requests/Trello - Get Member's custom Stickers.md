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
path: "/members/{id}/customStickers"
category: "Members"
writes_data: false
---
# Trello - Get Member's custom Stickers

**Get Member's custom Stickers** — `GET /members/{id}/customStickers`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Member's custom Stickers"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/customStickers
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Get a Member's uploaded stickers
