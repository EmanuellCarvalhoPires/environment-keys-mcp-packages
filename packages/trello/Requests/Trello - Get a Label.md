---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/labels
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/labels/{id}"
category: "Labels"
writes_data: false
---
# Trello - Get a Label

**Get a Label** — `GET /labels/{id}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Label"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/labels/{{param:id}}?fields={{param:fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `fields` (query, string, optional) — all or a comma-separated list of fields

## Original description

Get information about a single Label.
