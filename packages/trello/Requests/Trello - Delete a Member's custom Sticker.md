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
path: "/members/{id}/customStickers/{idSticker}"
category: "Members"
writes_data: true
---
# Trello - Delete a Member's custom Sticker

**Delete a Member's custom Sticker** — `DELETE /members/{id}/customStickers/{idSticker}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete a Member's custom Sticker"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/members/{{param:id}}/customStickers/{{param:idSticker}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idSticker` (path, string, required) — Value of idSticker in the path.

## Original description

Delete a Member's custom Sticker
