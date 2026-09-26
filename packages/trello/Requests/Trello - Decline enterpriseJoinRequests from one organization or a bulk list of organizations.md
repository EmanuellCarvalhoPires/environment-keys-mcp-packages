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
path: "/enterprises/${id}/enterpriseJoinRequest/bulk"
category: "Enterprises"
writes_data: true
---
# Trello - Decline enterpriseJoinRequests from one organization or a bulk list of organizations

**Decline enterpriseJoinRequests from one organization or a bulk list of organizations.** — `PUT /enterprises/${id}/enterpriseJoinRequest/bulk`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Decline enterpriseJoinRequests from one organization or a bulk list of organizations"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/enterprises/${{param:id}}/enterpriseJoinRequest/bulk?idOrganizations={{param:idOrganizations}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the Enterprise to retrieve.
- `idOrganizations` (query, string, required) — An array of IDs of an Organization resource.

## Original description

Decline enterpriseJoinRequests from one organization or bulk amount of organizations
