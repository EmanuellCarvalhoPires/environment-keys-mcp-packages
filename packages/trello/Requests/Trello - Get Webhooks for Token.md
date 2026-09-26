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
path: "/tokens/{token}/webhooks"
category: "Tokens"
writes_data: false
---
# Trello - Get Webhooks for Token

**Get Webhooks for Token** — `GET /tokens/{token}/webhooks`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Webhooks for Token"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/tokens/{{param:token}}/webhooks
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `token` (path, string, required) — Value of token in the path.

## Original description

Retrieve all webhooks created with a Token.
