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
path: "/enterprises/{id}/transferrable/organization/{idOrganization}"
category: "Enterprises"
writes_data: false
---
# Trello - Get whether an organization can be transferred to an enterprise

**Get whether an organization can be transferred to an enterprise.** — `GET /enterprises/{id}/transferrable/organization/{idOrganization}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get whether an organization can be transferred to an enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/enterprises/{{param:id}}/transferrable/organization/{{param:idOrganization}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the Enterprise to retrieve.
- `idOrganization` (path, string, required) — An ID of an Organization resource.

## Original description

Get whether an organization can be transferred to an enterprise.
