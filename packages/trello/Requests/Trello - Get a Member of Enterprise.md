---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/enterprises
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/enterprises/{id}/members/{idMember}"
category: "Enterprises"
writes_data: false
---
# Trello - Get a Member of Enterprise

**Get a Member of Enterprise** — `GET /enterprises/{id}/members/{idMember}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Member of Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/enterprises/{{param:id}}/members/{{param:idMember}}?fields={{param:fields}}&organization_fields={{param:organization_fields}}&board_fields={{param:board_fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the enterprise to retrieve.
- `idMember` (path, string, required) — An ID of a member resource.
- `fields` (query, string, optional) — A comma separated list of any valid values that the [nested member field resource]() accepts.
- `organization_fields` (query, string, optional) — Any valid value that the nested organization field resource accepts.
- `board_fields` (query, string, optional) — Any valid value that the nested board resource accepts.

## Original description

Get a specific member of an enterprise by ID.
