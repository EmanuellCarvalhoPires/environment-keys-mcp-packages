---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/notifications
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/notifications/{id}/{field}"
category: "Notifications"
writes_data: false
---
# Trello - Get a field of a Notification

**Get a field of a Notification** — `GET /notifications/{id}/{field}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a field of a Notification"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/notifications/{{param:id}}/{{param:field}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the notification
- `field` (path, string, required) — A notification field

## Original description

Get a specific property of a notification
