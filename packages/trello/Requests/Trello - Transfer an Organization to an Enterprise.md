---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/enterprises
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/enterprises/{id}/organizations"
category: "Enterprises"
writes_data: true
---
# Trello - Transfer an Organization to an Enterprise

**Transfer an Organization to an Enterprise.** — `PUT /enterprises/{id}/organizations`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Transfer an Organization to an Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/enterprises/{{param:id}}/organizations?idOrganization={{param:idOrganization}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the Enterprise to retrieve.
- `idOrganization` (query, string, required) — ID of Organization to be transferred to Enterprise.

## Original description

Transfer an organization to an enterprise.

 NOTE: For enterprises that have opted in to user management via AdminHub, this endpoint will result in the organization being added to the enterprise asynchronously. A 200 response only indicates receipt of the request, it does not indicate successful addition to the enterprise.
