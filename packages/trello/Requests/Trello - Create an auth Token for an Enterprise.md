---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/enterprises
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/enterprises/{id}/tokens"
category: "Enterprises"
writes_data: true
---
# Trello - Create an auth Token for an Enterprise

**Create an auth Token for an Enterprise.** — `POST /enterprises/{id}/tokens`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create an auth Token for an Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/enterprises/{{param:id}}/tokens?expiration={{param:expiration}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — ID of the enterprise to retrieve.
- `expiration` (query, string, optional) — One of: 1hour, 1day, 30days, never

## Original description

Create an auth Token for an Enterprise.
