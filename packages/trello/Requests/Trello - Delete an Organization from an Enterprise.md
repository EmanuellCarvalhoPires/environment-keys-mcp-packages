---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/enterprises
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/enterprises/{id}/organizations/{idOrg}"
category: "Enterprises"
writes_data: true
---
# Trello - Delete an Organization from an Enterprise

**Delete an Organization from an Enterprise.** — `DELETE /enterprises/{id}/organizations/{idOrg}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete an Organization from an Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/enterprises/{{param:id}}/organizations/{{param:idOrg}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — ID of the enterprise to retrieve.
- `idOrg` (path, string, required) — ID of the organization to be removed from the enterprise.

## Original description

Remove an organization from an enterprise.
