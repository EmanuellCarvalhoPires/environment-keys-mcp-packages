---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/boards/{id}/{field}"
category: "Boards"
writes_data: false
---
# Trello - Get a field on a Board

**Get a field on a Board** — `GET /boards/{id}/{field}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a field on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/boards/{{param:id}}/{{param:field}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the board.
- `field` (path, string, required) — The field you'd like to receive. Valid values: closed, dateLastActivity, dateLastView, desc, descData, idMemberCreator, idOrganization, invitations, invited, labelNames, memberships, name, pinned, pow…

## Original description

Get a single, specific field on a board
