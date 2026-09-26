---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/webhooks
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/webhooks/{id}"
category: "Webhooks"
writes_data: true
---
# Trello - Delete a Webhook

**Delete a Webhook** — `DELETE /webhooks/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete a Webhook"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/webhooks/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Delete a webhook by ID.
