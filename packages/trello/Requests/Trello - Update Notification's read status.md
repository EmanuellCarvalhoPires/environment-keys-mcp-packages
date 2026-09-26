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
path: "/notifications/{id}/unread"
category: "Notifications"
writes_data: true
---
# Trello - Update Notification's read status

**Update Notification's read status** — `PUT /notifications/{id}/unread`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update Notification's read status"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/notifications/{{param:id}}/unread?value={{param:value}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the notification
- `value` (query, string, optional) — Query parameter value.

## Original description

Update Notification's read status
