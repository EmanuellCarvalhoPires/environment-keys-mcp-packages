---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/members/{id}/notificationChannelSettings"
category: "Members"
writes_data: false
---
# Trello - Get a Member's notification channel settings

**Get a Member's notification channel settings** — `GET /members/{id}/notificationChannelSettings`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Member's notification channel settings"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/notificationChannelSettings
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Get a member's notification channel settings
