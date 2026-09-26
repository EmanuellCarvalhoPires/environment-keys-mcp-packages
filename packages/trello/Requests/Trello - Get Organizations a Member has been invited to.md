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
path: "/members/{id}/organizationsInvited"
category: "Members"
writes_data: false
---
# Trello - Get Organizations a Member has been invited to

**Get Organizations a Member has been invited to** — `GET /members/{id}/organizationsInvited`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Organizations a Member has been invited to"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/organizationsInvited?fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `fields` (query, string, optional) — all or a comma-separated list of organization fields

## Original description

Get a member's Workspaces they have been invited to
