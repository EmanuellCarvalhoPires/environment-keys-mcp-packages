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
path: "/enterprises/{id}/admins/{idMember}"
category: "Enterprises"
writes_data: true
---
# Trello - Remove a Member as admin from Enterprise

**Remove a Member as admin from Enterprise.** — `DELETE /enterprises/{id}/admins/{idMember}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Remove a Member as admin from Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/enterprises/{{param:id}}/admins/{{param:idMember}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — ID of the Enterprise to retrieve.
- `idMember` (path, string, required) — ID of the member to be removed as an admin from enterprise.

## Original description

Remove a member as admin from an enterprise.

 NOTE: This endpoint is not available to enterprises that have opted in to user management via AdminHub.
