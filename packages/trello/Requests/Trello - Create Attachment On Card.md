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
path: "/cards/{id}/attachments"
category: "Cards"
writes_data: true
---
# Trello - Create Attachment On Card

**Create Attachment On Card** — `POST /cards/{id}/attachments`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create Attachment On Card"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/cards/{{param:id}}/attachments?name={{param:name}}&file={{param:file}}&mimeType={{param:mimeType}}&url={{param:url}}&setCover={{param:setCover}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `name` (query, string, optional) — The name of the attachment. Max length 256.
- `file` (query, string, optional) — The file to attach, as multipart/form-data
- `mimeType` (query, string, optional) — The mimeType of the attachment. Max length 256
- `url` (query, string, optional) — A URL to attach. Must start with http:// or https://
- `setCover` (query, string, optional) — Determines whether to use the new attachment as a cover for the Card.

## Original description

Create an Attachment to a Card. See https://glitch.com/~trello-attachments-api for code examples. You may need to remix the project in order to view it.
