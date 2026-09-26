---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/members/{id}/notificationChannelSettings"
category: "Members"
writes_data: true
---
# Trello - Update blocked notification keys of Member on a channel

**Update blocked notification keys of Member on a channel** — `PUT /members/{id}/notificationChannelSettings`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update blocked notification keys of Member on a channel"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/members/{{param:id}}/notificationChannelSettings
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update blocked notification keys of Member on a specific channel
