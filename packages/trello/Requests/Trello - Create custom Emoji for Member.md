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
path: "/members/{id}/customEmoji"
category: "Members"
writes_data: true
---
# Trello - Create custom Emoji for Member

**Create custom Emoji for Member** — `POST /members/{id}/customEmoji`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create custom Emoji for Member"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/members/{{param:id}}/customEmoji?file={{param:file}}&name={{param:name}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `file` (query, string, required) — Query parameter file.
- `name` (query, string, required) — Name for the emoji. 2 - 64 characters

## Original description

Create a new custom Emoji
