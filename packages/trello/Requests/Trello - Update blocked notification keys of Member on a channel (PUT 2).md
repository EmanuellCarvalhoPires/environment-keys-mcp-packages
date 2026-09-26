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
path: "/members/{id}/notificationChannelSettings/{channel}/{blockedKeys}"
category: "Members"
writes_data: true
---
# Trello - Update blocked notification keys of Member on a channel (PUT 2)

**Update blocked notification keys of Member on a channel** — `PUT /members/{id}/notificationChannelSettings/{channel}/{blockedKeys}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update blocked notification keys of Member on a channel (PUT 2)"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/members/{{param:id}}/notificationChannelSettings/{{param:channel}}/{{param:blockedKeys}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `channel` (path, string, required) — Value of channel in the path.
- `blockedKeys` (path, string, required) — Value of blockedKeys in the path.

## Original description

Update blocked notification keys of Member on a specific channel
