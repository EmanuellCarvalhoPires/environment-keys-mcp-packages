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
path: "/members/{id}/notifications"
category: "Members"
writes_data: false
---
# Trello - Get Member's Notifications

**Get Member's Notifications** — `GET /members/{id}/notifications`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Member's Notifications"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/notifications?entities={{param:entities}}&display={{param:display}}&filter={{param:filter}}&read_filter={{param:read_filter}}&fields={{param:fields}}&limit={{param:limit}}&page={{param:page}}&before={{param:before}}&since={{param:since}}&memberCreator={{param:memberCreator}}&memberCreator_fields={{param:memberCreator_fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `entities` (query, string, optional) — Query parameter entities.
- `display` (query, string, optional) — Query parameter display.
- `filter` (query, string, optional) — Query parameter filter.
- `read_filter` (query, string, optional) — One of: all, read, unread
- `fields` (query, string, optional) — all or a comma-separated list of notification fields
- `limit` (query, string, optional) — Max 1000
- `page` (query, string, optional) — Max 100
- `before` (query, string, optional) — A notification ID
- `since` (query, string, optional) — A notification ID
- `memberCreator` (query, string, optional) — Query parameter memberCreator.
- `memberCreator_fields` (query, string, optional) — all or a comma-separated list of member fields

## Original description

Get a member's notifications
