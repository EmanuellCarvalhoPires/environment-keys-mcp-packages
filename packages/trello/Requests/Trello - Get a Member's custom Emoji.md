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
path: "/members/{id}/customEmoji/{idEmoji}"
category: "Members"
writes_data: false
---
# Trello - Get a Member's custom Emoji

**Get a Member's custom Emoji** — `GET /members/{id}/customEmoji/{idEmoji}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Member's custom Emoji"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/customEmoji/{{param:idEmoji}}?fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `idEmoji` (path, string, required) — The ID of the custom emoji
- `fields` (query, string, optional) — all or a comma-separated list of name, url

## Original description

Get a Member's custom Emoji
