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
path: "/members/{id}/tokens"
category: "Members"
writes_data: false
---
# Trello - Get Member's Tokens

**Get Member's Tokens** — `GET /members/{id}/tokens`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Member's Tokens"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/tokens?webhooks={{param:webhooks}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `webhooks` (query, string, optional) — Whether to include webhooks

## Original description

List a members app tokens
