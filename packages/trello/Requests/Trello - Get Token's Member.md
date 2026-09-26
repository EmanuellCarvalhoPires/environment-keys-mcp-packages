---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/tokens
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/tokens/{token}/member"
category: "Tokens"
writes_data: false
---
# Trello - Get Token's Member

**Get Token's Member** — `GET /tokens/{token}/member`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Token's Member"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/tokens/{{param:token}}/member?fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `token` (path, string, required) — Value of token in the path.
- `fields` (query, string, optional) — all or a comma-separated list of valid fields for Member Object.

## Original description

Retrieve information about a token's owner by token.
