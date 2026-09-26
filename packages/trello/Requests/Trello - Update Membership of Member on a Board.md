---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/boards/{id}/memberships/{idMembership}"
category: "Boards"
writes_data: true
---
# Trello - Update Membership of Member on a Board

**Update Membership of Member on a Board** — `PUT /boards/{id}/memberships/{idMembership}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update Membership of Member on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/boards/{{param:id}}/memberships/{{param:idMembership}}?type={{param:type}}&member_fields={{param:member_fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The id of the board to update
- `idMembership` (path, string, required) — The id of a membership that should be added to this board.
- `type` (query, string, required) — One of: admin, normal, observer. Determines the type of member that this membership will be to this board.
- `member_fields` (query, string, optional) — Valid values: all, avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username

## Original description

Update an existing board by id
