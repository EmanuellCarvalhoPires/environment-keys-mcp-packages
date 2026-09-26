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
path: "/members/{id}/organizations"
category: "Members"
writes_data: false
---
# Trello - Get Member's Organizations

**Get Member's Organizations** — `GET /members/{id}/organizations`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Member's Organizations"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/organizations?filter={{param:filter}}&fields={{param:fields}}&paid_account={{param:paid_account}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `filter` (query, string, optional) — One of: all, members, none, public (Note: members filters to only private Workspaces)
- `fields` (query, string, optional) — all or a comma-separated list of organization fields
- `paid_account` (query, string, optional) — Whether or not to include paid account information in the returned workspace object

## Original description

Get a member's Workspaces
