---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/cards/{id}/actions/comments"
category: "Cards"
writes_data: true
---
# Trello - Add a new comment to a Card

**Add a new comment to a Card** — `POST /cards/{id}/actions/comments`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Add a new comment to a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/cards/{{param:id}}/actions/comments?text={{param:text}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `text` (query, string, required) — The comment

## Original description

Add a new comment to a card
