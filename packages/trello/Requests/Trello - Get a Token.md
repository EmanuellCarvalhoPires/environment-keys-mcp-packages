---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/tokens
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/tokens/{token}"
category: "Tokens"
writes_data: false
---
# Trello - Get a Token

**Get a Token** — `GET /tokens/{token}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Token"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/tokens/{{param:token}}?fields={{param:fields}}&webhooks={{param:webhooks}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `token` (path, string, required) — Value of token in the path.
- `fields` (query, string, optional) — all or a comma-separated list of dateCreated, dateExpires, idMember, identifier, permissions
- `webhooks` (query, string, optional) — Determines whether to include webhooks.

## Original description

Retrieve information about a token.
