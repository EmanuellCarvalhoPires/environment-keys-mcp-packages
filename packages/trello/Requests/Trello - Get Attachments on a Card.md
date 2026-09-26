---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/cards/{id}/attachments"
category: "Cards"
writes_data: false
---
# Trello - Get Attachments on a Card

**Get Attachments on a Card** — `GET /cards/{id}/attachments`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Attachments on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/cards/{{param:id}}/attachments?fields={{param:fields}}&filter={{param:filter}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `fields` (query, string, optional) — all or a comma-separated list of attachment fields
- `filter` (query, string, optional) — Use cover to restrict to just the cover attachment

## Original description

List the attachments on a card
