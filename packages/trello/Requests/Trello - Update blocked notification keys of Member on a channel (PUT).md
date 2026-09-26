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
path: "/members/{id}/notificationChannelSettings/{channel}"
category: "Members"
writes_data: true
---
# Trello - Update blocked notification keys of Member on a channel (PUT)

**Update blocked notification keys of Member on a channel** — `PUT /members/{id}/notificationChannelSettings/{channel}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update blocked notification keys of Member on a channel (PUT)"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/members/{{param:id}}/notificationChannelSettings/{{param:channel}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `channel` (path, string, required) — Value of channel in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update blocked notification keys of Member on a specific channel
