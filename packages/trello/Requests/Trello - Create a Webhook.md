---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/webhooks
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/webhooks/"
category: "Webhooks"
writes_data: true
---
# Trello - Create a Webhook

**Create a Webhook** — `POST /webhooks/`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a Webhook"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/webhooks/?description={{param:description}}&callbackURL={{param:callbackURL}}&idModel={{param:idModel}}&active={{param:active}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `description` (query, string, optional) — A string with a length from 0 to 16384.
- `callbackURL` (query, string, required) — A valid URL that is reachable with a HEAD and POST request.
- `idModel` (query, string, required) — ID of the model to be monitored
- `active` (query, string, optional) — Determines whether the webhook is active and sending POST requests.

## Original description

Create a new webhook.
