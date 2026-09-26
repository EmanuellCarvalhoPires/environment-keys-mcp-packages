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
path: "/members/{id}/customStickers/{idSticker}"
category: "Members"
writes_data: false
---
# Trello - Get a Member's custom Sticker

**Get a Member's custom Sticker** — `GET /members/{id}/customStickers/{idSticker}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Member's custom Sticker"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/customStickers/{{param:idSticker}}?fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idSticker` (path, string, required) — Value of idSticker in the path.
- `fields` (query, string, optional) — all or a comma-separated list of scaled, url

## Original description

Get a Member's custom Sticker
