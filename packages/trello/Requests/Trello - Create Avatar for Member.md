---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/members/{id}/avatar"
category: "Members"
writes_data: true
---
# Trello - Create Avatar for Member

**Create Avatar for Member** — `POST /members/{id}/avatar`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create Avatar for Member"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/members/{{param:id}}/avatar?file={{param:file}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `file` (query, string, required) — Query parameter file.

## Original description

Create a new avatar for a member
