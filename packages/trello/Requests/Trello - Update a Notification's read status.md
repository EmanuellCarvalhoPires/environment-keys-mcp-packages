---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/notifications
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/notifications/{id}"
category: "Notifications"
writes_data: true
---
# Trello - Update a Notification's read status

**Update a Notification's read status** — `PUT /notifications/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a Notification's read status"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/notifications/{{param:id}}?unread={{param:unread}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the notification
- `unread` (query, string, optional) — Whether the notification should be marked as read or not

## Original description

Update the read status of a notification
