---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/webhooks
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/webhooks/{id}"
category: "Webhooks"
writes_data: true
---
# Trello - Update a Webhook

**Update a Webhook** — `PUT /webhooks/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a Webhook"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/webhooks/{{param:id}}?description={{param:description}}&callbackURL={{param:callbackURL}}&idModel={{param:idModel}}&active={{param:active}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `description` (query, string, optional) — A string with a length from 0 to 16384.
- `callbackURL` (query, string, optional) — A valid URL that is reachable with a HEAD and POST request.
- `idModel` (query, string, optional) — ID of the model to be monitored
- `active` (query, string, optional) — Determines whether the webhook is active and sending POST requests.

## Original description

Update a webhook by ID.
