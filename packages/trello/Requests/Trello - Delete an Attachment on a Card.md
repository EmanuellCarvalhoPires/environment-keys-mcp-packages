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
path: "/cards/{id}/attachments/{idAttachment}"
category: "Cards"
writes_data: true
---
# Trello - Delete an Attachment on a Card

**Delete an Attachment on a Card** — `DELETE /cards/{id}/attachments/{idAttachment}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete an Attachment on a Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/cards/{{param:id}}/attachments/{{param:idAttachment}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Card
- `idAttachment` (path, string, required) — The ID of the attachment to delete

## Original description

Delete an Attachment
