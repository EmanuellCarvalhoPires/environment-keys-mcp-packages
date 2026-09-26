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
path: "/notifications/{id}/member"
category: "Notifications"
writes_data: false
---
# Trello - Get the Member a Notification is about (not the creator)

**Get the Member a Notification is about (not the creator)** — `GET /notifications/{id}/member`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get the Member a Notification is about (not the creator)"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/notifications/{{param:id}}/member?fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the notification
- `fields` (query, string, optional) — all or a comma-separated list of member fields

## Original description

Get the member (not the creator) a notification is about
