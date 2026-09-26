---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/notifications
  - api/operation/action
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/notifications/all/read"
category: "Notifications"
writes_data: true
---
# Trello - Mark all Notifications as read

**Mark all Notifications as read** — `POST /notifications/all/read`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Mark all Notifications as read"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/notifications/all/read?read={{param:read}}&ids={{param:ids}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `read` (query, string, optional) — Boolean to specify whether to mark as read or unread (defaults to true, marking as read)
- `ids` (query, string, optional) — A comma-seperated list of IDs. Allows specifying an array of notification IDs to change the read state for.

## Original description

Mark all notifications as read
