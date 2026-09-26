---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/members/{id}/boardBackgrounds/{idBackground}"
category: "Members"
writes_data: false
---
# Trello - Get a boardBackground of a Member

**Get a boardBackground of a Member** — `GET /members/{id}/boardBackgrounds/{idBackground}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a boardBackground of a Member"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/members/{{param:id}}/boardBackgrounds/{{param:idBackground}}?fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idBackground` (path, string, required) — Value of idBackground in the path.
- `fields` (query, string, optional) — all or a comma-separated list of: brightness, fullSizeUrl, scaled, tile

## Original description

Get a member's board background
