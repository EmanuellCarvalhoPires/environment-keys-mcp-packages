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
path: "/members/{id}/boardBackgrounds"
category: "Members"
writes_data: true
---
# Trello - Upload new boardBackground for Member

**Upload new boardBackground for Member** — `POST /members/{id}/boardBackgrounds`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Upload new boardBackground for Member"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/members/{{param:id}}/boardBackgrounds?file={{param:file}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `file` (query, string, required) — Query parameter file.

## Original description

Upload a new boardBackground
