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
path: "/enterprises/{id}/organizations"
category: "Enterprises"
writes_data: false
---
# Trello - Get Organizations of an Enterprise

**Get Organizations of an Enterprise** — `GET /enterprises/{id}/organizations`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Organizations of an Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/enterprises/{{param:id}}/organizations?fields={{param:fields}}&filter={{param:filter}}&startIndex={{param:startIndex}}&count={{param:count}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the Enterprise to retrieve.
- `fields` (query, string, optional) — comma-separated list of organization fields
- `filter` (query, string, optional) — Query parameter filter.
- `startIndex` (query, string, optional) — Any integer greater than and equal to 1.
- `count` (query, string, optional) — Any integer between 0 and 100.

## Original description

Get the organizations of an enterprise.
