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
path: "/notifications/{id}/memberCreator"
category: "Notifications"
writes_data: false
---
# Trello - Get the Member who created the Notification

**Get the Member who created the Notification** — `GET /notifications/{id}/memberCreator`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get the Member who created the Notification"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/notifications/{{param:id}}/memberCreator?fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the notification
- `fields` (query, string, optional) — all or a comma-separated list of member fields

## Original description

Get the member who created the notification
