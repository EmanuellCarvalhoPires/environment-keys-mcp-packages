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
path: "/members/{id}/cards"
category: "Members"
writes_data: false
---
# Trello - Get Cards the Member is on

**Get Cards the Member is on** — `GET /members/{id}/cards`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Cards the Member is on"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/cards?filter={{param:filter}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `filter` (query, string, optional) — One of: all, closed, complete, incomplete, none, open, visible

## Original description

Gets the cards a member is on
