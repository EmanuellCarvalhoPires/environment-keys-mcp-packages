---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/notifications
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/notifications/{id}/card"
category: "Notifications"
writes_data: false
---
# Trello - Get the Card a Notification is on

**Get the Card a Notification is on** — `GET /notifications/{id}/card`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get the Card a Notification is on"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/notifications/{{param:id}}/card?fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the notification
- `fields` (query, string, optional) — all or a comma-separated list of card fields

## Original description

Get the card a notification is associated with
