---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/webhooks
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/webhooks/{id}/{field}"
category: "Webhooks"
writes_data: false
---
# Trello - Get a field on a Webhook

**Get a field on a Webhook** — `GET /webhooks/{id}/{field}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a field on a Webhook"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/webhooks/{{param:id}}/{{param:field}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — ID of the webhook.
- `field` (path, string, required) — Field to retrieve. One of: active, callbackURL, description, idModel

## Original description

Get a field on a Webhook
