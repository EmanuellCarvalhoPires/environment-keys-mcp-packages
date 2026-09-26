---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/cards/{id}/actions/{idAction}/comments"
category: "Cards"
writes_data: true
---
# Trello - Update Comment Action on a Card

**Update Comment Action on a Card** — `PUT /cards/{id}/actions/{idAction}/comments`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update Comment Action on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/cards/{{param:id}}/actions/{{param:idAction}}/comments?text={{param:text}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idAction` (path, string, required) — Value of idAction in the path.
- `text` (query, string, required) — The new text for the comment

## Original description

Update an existing comment
