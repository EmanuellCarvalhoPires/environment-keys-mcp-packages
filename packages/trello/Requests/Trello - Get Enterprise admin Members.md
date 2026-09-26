---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/enterprises
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/enterprises/{id}/admins"
category: "Enterprises"
writes_data: false
---
# Trello - Get Enterprise admin Members

**Get Enterprise admin Members** — `GET /enterprises/{id}/admins`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Enterprise admin Members"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/enterprises/{{param:id}}/admins?fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the enterprise to retrieve.
- `fields` (query, string, optional) — Any valid value that the [nested member field resource]() accepts.

## Original description

Get an enterprise's admin members.
