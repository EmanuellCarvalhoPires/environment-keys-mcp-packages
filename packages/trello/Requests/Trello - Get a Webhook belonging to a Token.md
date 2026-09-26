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
path: "/tokens/{token}/webhooks/{idWebhook}"
category: "Tokens"
writes_data: false
---
# Trello - Get a Webhook belonging to a Token

**Get a Webhook belonging to a Token** — `GET /tokens/{token}/webhooks/{idWebhook}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Webhook belonging to a Token"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/tokens/{{param:token}}/webhooks/{{param:idWebhook}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `token` (path, string, required) — Value of token in the path.
- `idWebhook` (path, string, required) — Value of idWebhook in the path.

## Original description

Retrieve a webhook created with a Token.
