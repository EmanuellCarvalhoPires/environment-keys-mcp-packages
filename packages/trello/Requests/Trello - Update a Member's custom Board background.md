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
path: "/members/{id}/boardBackgrounds/{idBackground}"
category: "Members"
writes_data: true
---
# Trello - Update a Member's custom Board background

**Update a Member's custom Board background** — `PUT /members/{id}/boardBackgrounds/{idBackground}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a Member's custom Board background"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/members/{{param:id}}/boardBackgrounds/{{param:idBackground}}?brightness={{param:brightness}}&tile={{param:tile}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idBackground` (path, string, required) — Value of idBackground in the path.
- `brightness` (query, string, optional) — One of: dark, light, unknown
- `tile` (query, string, optional) — Whether the background should be tiled

## Original description

Update a board background
