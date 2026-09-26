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
path: "/boards/{id}/members"
category: "Boards"
writes_data: true
---
# Trello - Invite Member to Board via email

**Invite Member to Board via email** — `PUT /boards/{id}/members`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Invite Member to Board via email"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/boards/{{param:id}}/members?email={{param:email}}&type={{param:type}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `email` (query, string, required) — The email address of a user to add as a member of the board.
- `type` (query, string, optional) — Valid values: admin, normal, observer. Determines what type of member the user being added should be of the board.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Invite a Member to a Board via their email address.
