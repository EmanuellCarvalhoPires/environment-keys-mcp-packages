---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/tokens
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/tokens/{token}/webhooks/{idWebhook}"
category: "Tokens"
writes_data: true
---
# Trello - Delete a Webhook created by Token

**Delete a Webhook created by Token** — `DELETE /tokens/{token}/webhooks/{idWebhook}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete a Webhook created by Token"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/tokens/{{param:token}}/webhooks/{{param:idWebhook}}
Authorization: {{service.auth_token}}
```

## Parameters

- `token` (path, string, required) — Value of token in the path.
- `idWebhook` (path, string, required) — Value of idWebhook in the path.

## Original description

Delete a webhook created with given token.
