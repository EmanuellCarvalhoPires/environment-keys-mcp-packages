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
path: "/notifications/{id}/organization"
category: "Notifications"
writes_data: false
---
# Trello - Get a Notification's associated Organization

**Get a Notification's associated Organization** — `GET /notifications/{id}/organization`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Notification's associated Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/notifications/{{param:id}}/organization?fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the notification
- `fields` (query, string, optional) — all or a comma-separated list of organization fields

## Original description

Get the organization a notification is associated with
