---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/boards/{id}/memberships"
category: "Boards"
writes_data: false
---
# Trello - Get Memberships of a Board

**Get Memberships of a Board** — `GET /boards/{id}/memberships`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Memberships of a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}/memberships?filter={{param:filter}}&activity={{param:activity}}&orgMemberType={{param:orgMemberType}}&member={{param:member}}&member_fields={{param:member_fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the board
- `filter` (query, string, optional) — One of admins, all, none, normal
- `activity` (query, string, optional) — Works for premium organizations only.
- `orgMemberType` (query, string, optional) — Shows the type of member to the org the user is. For instance, an org admin will have a orgMemberType of admin.
- `member` (query, string, optional) — Determines whether to include a nested member object.
- `member_fields` (query, string, optional) — Fields to show if member=true. Valid values: nested member resource fields.

## Original description

Get information about the memberships users have to the board.
