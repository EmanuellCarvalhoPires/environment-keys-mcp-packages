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
path: "/cards/{id}/checklists/{idChecklist}"
category: "Cards"
writes_data: true
---
# Trello - Delete a Checklist on a Card

**Delete a Checklist on a Card** — `DELETE /cards/{id}/checklists/{idChecklist}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete a Checklist on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/cards/{{param:id}}/checklists/{{param:idChecklist}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `idChecklist` (path, string, required) — The ID of the checklist to delete

## Original description

Delete a checklist from a card
