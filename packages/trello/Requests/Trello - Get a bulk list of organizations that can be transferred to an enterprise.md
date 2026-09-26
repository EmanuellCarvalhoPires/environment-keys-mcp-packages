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
path: "/enterprises/{id}/transferrable/bulk/{idOrganizations}"
category: "Enterprises"
writes_data: false
---
# Trello - Get a bulk list of organizations that can be transferred to an enterprise

**Get a bulk list of organizations that can be transferred to an enterprise.** — `GET /enterprises/{id}/transferrable/bulk/{idOrganizations}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a bulk list of organizations that can be transferred to an enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/enterprises/{{param:id}}/transferrable/bulk/{{param:idOrganizations}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the Enterprise to retrieve.
- `idOrganizations` (path, string, required) — An array of IDs of an Organization resource.

## Original description

Get a list of organizations that can be transferred to an enterprise when given a bulk list of organizations.
