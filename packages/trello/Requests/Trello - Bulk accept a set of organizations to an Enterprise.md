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
path: "/enterprises/{id}/organizations/bulk/{idOrganizations}"
category: "Enterprises"
writes_data: false
---
# Trello - Bulk accept a set of organizations to an Enterprise

**Bulk accept a set of organizations to an Enterprise.** — `GET /enterprises/{id}/organizations/bulk/{idOrganizations}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Bulk accept a set of organizations to an Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/enterprises/{{param:id}}/organizations/bulk/{{param:idOrganizations}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the enterprise to retrieve.
- `idOrganizations` (path, string, required) — An array of IDs of the organizations to be removed from the enterprise.

## Original description

Accept an array of organizations to an enterprise.

 NOTE: For enterprises that have opted in to user management via AdminHub, this endpoint will result in organizations being added to the enterprise asynchronously. A 200 response only indicates receipt of the request, it does not indicate successful addition to the enterprise.
