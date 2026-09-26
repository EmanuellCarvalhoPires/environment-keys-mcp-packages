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
path: "/members/{id}/customEmoji"
category: "Members"
writes_data: false
---
# Trello - Get a Member's customEmojis

**Get a Member's customEmojis** — `GET /members/{id}/customEmoji`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Member's customEmojis"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/customEmoji
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Get a Member's uploaded custom Emojis
