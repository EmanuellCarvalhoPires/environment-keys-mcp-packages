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
path: "/cards/{id}/labels"
category: "Cards"
writes_data: true
---
# Trello - Create a new Label on a Card

**Create a new Label on a Card** — `POST /cards/{id}/labels`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a new Label on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/cards/{{param:id}}/labels?color={{param:color}}&name={{param:name}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `color` (query, string, required) — A valid label color or null. See labels
- `name` (query, string, optional) — A name for the label

## Original description

Create a new label for the board and add it to the given card.
