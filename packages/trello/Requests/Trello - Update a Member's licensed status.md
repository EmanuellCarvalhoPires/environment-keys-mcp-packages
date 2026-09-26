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
path: "/enterprises/{id}/members/{idMember}/licensed"
category: "Enterprises"
writes_data: true
---
# Trello - Update a Member's licensed status

**Update a Member's licensed status** — `PUT /enterprises/{id}/members/{idMember}/licensed`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a Member's licensed status"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/enterprises/{{param:id}}/members/{{param:idMember}}/licensed?value={{param:value}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the Enterprise.
- `idMember` (path, string, required) — The ID of the Member
- `value` (query, string, required) — Boolean value to determine whether the user should be given an Enterprise license (true) or not (false).

## Original description

This endpoint is used to update whether the provided Member should use one of the Enterprise's available licenses or not. Revoking a license will deactivate a Member of an Enterprise. 

 NOTE: Revoking of licenses is not possible for enterprises that have opted in to user management via AdminHub.
