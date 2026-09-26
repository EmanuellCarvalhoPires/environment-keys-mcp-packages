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
path: "/members/{id}/boardStars"
category: "Members"
writes_data: true
---
# Trello - Create Star for Board

**Create Star for Board** — `POST /members/{id}/boardStars`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create Star for Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/members/{{param:id}}/boardStars?idBoard={{param:idBoard}}&pos={{param:pos}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `idBoard` (query, string, required) — The ID of the board to star
- `pos` (query, string, required) — The position of the newly starred board. top, bottom, or a positive float.

## Original description

Star a new board on behalf of a Member
