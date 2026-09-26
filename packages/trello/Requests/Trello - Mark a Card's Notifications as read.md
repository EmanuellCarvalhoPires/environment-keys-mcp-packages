---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/action
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/cards/{id}/markAssociatedNotificationsRead"
category: "Cards"
writes_data: true
---
# Trello - Mark a Card's Notifications as read

**Mark a Card's Notifications as read** — `POST /cards/{id}/markAssociatedNotificationsRead`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Mark a Card's Notifications as read"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/cards/{{param:id}}/markAssociatedNotificationsRead
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Card

## Original description

Mark notifications about this card as read
