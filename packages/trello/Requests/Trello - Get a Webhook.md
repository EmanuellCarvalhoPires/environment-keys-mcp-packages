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
path: "/webhooks/{id}"
category: "Webhooks"
writes_data: false
---
# Trello - Get a Webhook

**Get a Webhook** — `GET /webhooks/{id}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Webhook"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/webhooks/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Get a webhook by ID. You must use the token query parameter and pass in the token the webhook was created under, or else you will encounter a 'webhook does not belong to token' error.
