---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/members/{id}/customBoardBackgrounds/{idBackground}"
category: "Members"
writes_data: true
---
# Trello - Delete custom Board Background of Member

**Delete custom Board Background of Member** — `DELETE /members/{id}/customBoardBackgrounds/{idBackground}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete custom Board Background of Member"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/members/{{param:id}}/customBoardBackgrounds/{{param:idBackground}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idBackground` (path, string, required) — Value of idBackground in the path.

## Original description

Delete a specific custom board background
