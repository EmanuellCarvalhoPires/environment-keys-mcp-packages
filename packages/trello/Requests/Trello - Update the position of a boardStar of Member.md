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
path: "/members/{id}/boardStars/{idStar}"
category: "Members"
writes_data: true
---
# Trello - Update the position of a boardStar of Member

**Update the position of a boardStar of Member** — `PUT /members/{id}/boardStars/{idStar}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update the position of a boardStar of Member"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/members/{{param:id}}/boardStars/{{param:idStar}}?pos={{param:pos}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idStar` (path, string, required) — Value of idStar in the path.
- `pos` (query, string, optional) — New position for the starred board. top, bottom, or a positive float.

## Original description

Update the position of a starred board
