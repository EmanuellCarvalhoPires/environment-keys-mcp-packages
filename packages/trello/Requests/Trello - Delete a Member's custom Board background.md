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
path: "/members/{id}/boardBackgrounds/{idBackground}"
category: "Members"
writes_data: true
---
# Trello - Delete a Member's custom Board background

**Delete a Member's custom Board background** — `DELETE /members/{id}/boardBackgrounds/{idBackground}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete a Member's custom Board background"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/members/{{param:id}}/boardBackgrounds/{{param:idBackground}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idBackground` (path, string, required) — Value of idBackground in the path.

## Original description

Delete a board background
