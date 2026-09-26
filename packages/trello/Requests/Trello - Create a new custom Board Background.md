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
path: "/members/{id}/customBoardBackgrounds"
category: "Members"
writes_data: true
---
# Trello - Create a new custom Board Background

**Create a new custom Board Background** — `POST /members/{id}/customBoardBackgrounds`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a new custom Board Background"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/members/{{param:id}}/customBoardBackgrounds?file={{param:file}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `file` (query, string, required) — Query parameter file.

## Original description

Upload a new custom board background
