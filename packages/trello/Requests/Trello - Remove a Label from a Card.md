---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/cards
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/cards/{id}/idLabels/{idLabel}"
category: "Cards"
writes_data: true
---
# Trello - Remove a Label from a Card

**Remove a Label from a Card** — `DELETE /cards/{id}/idLabels/{idLabel}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Remove a Label from a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/cards/{{param:id}}/idLabels/{{param:idLabel}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `idLabel` (path, string, required) — The ID of the label to remove

## Original description

Remove a label from a card
