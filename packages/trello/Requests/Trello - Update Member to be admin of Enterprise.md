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
path: "/enterprises/{id}/admins/{idMember}"
category: "Enterprises"
writes_data: true
---
# Trello - Update Member to be admin of Enterprise

**Update Member to be admin of Enterprise** — `PUT /enterprises/{id}/admins/{idMember}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update Member to be admin of Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/enterprises/{{param:id}}/admins/{{param:idMember}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — ID of the enterprise to retrieve.
- `idMember` (path, string, required) — ID of member to be made an admin of enterprise.

## Original description

Make Member an admin of Enterprise.

 NOTE: This endpoint is not available to enterprises that have opted in to user management via AdminHub.
