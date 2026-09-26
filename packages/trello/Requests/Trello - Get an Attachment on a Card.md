---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/cards/{id}/attachments/{idAttachment}"
category: "Cards"
writes_data: false
---
# Trello - Get an Attachment on a Card

**Get an Attachment on a Card** — `GET /cards/{id}/attachments/{idAttachment}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get an Attachment on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/cards/{{param:id}}/attachments/{{param:idAttachment}}?fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idAttachment` (path, string, required) — Value of idAttachment in the path.
- `fields` (query, string, optional) — The Attachment fields to be included in the response.

## Original description

Get a specific Attachment on a Card.
