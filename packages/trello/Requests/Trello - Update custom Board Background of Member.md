---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/members/{id}/customBoardBackgrounds/{idBackground}"
category: "Members"
writes_data: true
---
# Trello - Update custom Board Background of Member

**Update custom Board Background of Member** — `PUT /members/{id}/customBoardBackgrounds/{idBackground}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update custom Board Background of Member"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/members/{{param:id}}/customBoardBackgrounds/{{param:idBackground}}?brightness={{param:brightness}}&tile={{param:tile}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idBackground` (path, string, required) — Value of idBackground in the path.
- `brightness` (query, string, optional) — One of: dark, light, unknown
- `tile` (query, string, optional) — Whether to tile the background

## Original description

Update a specific custom board background
