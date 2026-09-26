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
path: "/members/{id}/boardsInvited"
category: "Members"
writes_data: false
---
# Trello - Get Boards the Member has been invited to

**Get Boards the Member has been invited to** — `GET /members/{id}/boardsInvited`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Boards the Member has been invited to"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/boardsInvited?fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `fields` (query, string, optional) — all or a comma-separated list of board fields

## Original description

Get the boards the member has been invited to
