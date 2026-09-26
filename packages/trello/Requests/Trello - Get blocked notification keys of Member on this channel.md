---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/members/{id}/notificationChannelSettings/{channel}"
category: "Members"
writes_data: false
---
# Trello - Get blocked notification keys of Member on this channel

**Get blocked notification keys of Member on this channel** — `GET /members/{id}/notificationChannelSettings/{channel}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get blocked notification keys of Member on this channel"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/notificationChannelSettings/{{param:channel}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `channel` (path, string, required) — Value of channel in the path.

## Original description

Get blocked notification keys of Member on a specific channel
