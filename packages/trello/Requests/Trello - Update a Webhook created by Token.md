---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/tokens
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/tokens/{token}/webhooks/{idWebhook}"
category: "Tokens"
writes_data: true
---
# Trello - Update a Webhook created by Token

**Update a Webhook created by Token** — `PUT /tokens/{token}/webhooks/{idWebhook}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a Webhook created by Token"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/tokens/{{param:token}}/webhooks/{{param:idWebhook}}?description={{param:description}}&callbackURL={{param:callbackURL}}&idModel={{param:idModel}}
Authorization: {{service.auth_token}}
```

## Parameters

- `token` (path, string, required) — Value of token in the path.
- `idWebhook` (path, string, required) — Value of idWebhook in the path.
- `description` (query, string, optional) — A description to be displayed when retrieving information about the webhook.
- `callbackURL` (query, string, optional) — The URL that the webhook should POST information to.
- `idModel` (query, string, optional) — ID of the object that the webhook is on.

## Original description

Update a Webhook created by Token
