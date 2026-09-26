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
path: "/members/{id}/boardBackgrounds"
category: "Members"
writes_data: false
---
# Trello - Get Member's custom Board backgrounds

**Get Member's custom Board backgrounds** — `GET /members/{id}/boardBackgrounds`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Member's custom Board backgrounds"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/boardBackgrounds?filter={{param:filter}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `filter` (query, string, optional) — One of: all, custom, default, none, premium

## Original description

Get a member's custom board backgrounds
