---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/tokens
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/tokens/{token}/webhooks"
category: "Tokens"
writes_data: true
---
# Trello - Create Webhooks for Token

**Create Webhooks for Token** — `POST /tokens/{token}/webhooks`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create Webhooks for Token"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/tokens/{{param:token}}/webhooks?description={{param:description}}&callbackURL={{param:callbackURL}}&idModel={{param:idModel}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `token` (path, string, required) — Value of token in the path.
- `description` (query, string, optional) — A description to be displayed when retrieving information about the webhook.
- `callbackURL` (query, string, required) — The URL that the webhook should POST information to.
- `idModel` (query, string, required) — ID of the object to create a webhook on.

## Original description

Create a new webhook for a Token.
