---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/customfields
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/customFields"
category: "CustomFields"
writes_data: true
---
# Trello - Create a new Custom Field on a Board

**Create a new Custom Field on a Board** — `POST /customFields`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a new Custom Field on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/customFields
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create a new Custom Field on a board.
