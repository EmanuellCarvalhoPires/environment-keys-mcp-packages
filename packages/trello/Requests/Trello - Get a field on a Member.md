---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/members/{id}/{field}"
category: "Members"
writes_data: false
---
# Trello - Get a field on a Member

**Get a field on a Member** — `GET /members/{id}/{field}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a field on a Member"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/{{param:field}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `field` (path, string, required) — One of the member fields

## Original description

Get a particular property of a member
