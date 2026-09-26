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
path: "/members/{id}/actions"
category: "Members"
writes_data: false
---
# Trello - Get a Member's Actions

**Get a Member's Actions** — `GET /members/{id}/actions`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Member's Actions"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/actions?filter={{param:filter}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `filter` (query, string, optional) — A comma-separated list of action types.

## Original description

List the actions for a member
