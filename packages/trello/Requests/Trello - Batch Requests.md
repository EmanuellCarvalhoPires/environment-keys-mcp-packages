---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/batch
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/batch"
category: "Batch"
writes_data: false
---
# Trello - Batch Requests

**Batch Requests** — `GET /batch`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Batch Requests"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/batch?urls={{param:urls}}
Authorization: {{service.auth_token}}
```

## Parameters

- `urls` (query, string, required) — A list of API routes. Maximum of 10 routes allowed. The routes should begin with a forward slash and should not include the API version number - e.g. "urls=/members/trello,/cards/[cardId]"

## Original description

Make up to 10 GET requests in a single, batched API call.
