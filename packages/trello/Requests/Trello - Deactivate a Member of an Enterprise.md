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
path: "/enterprises/{id}/members/{idMember}/deactivated"
category: "Enterprises"
writes_data: true
---
# Trello - Deactivate a Member of an Enterprise

**Deactivate a Member of an Enterprise.** — `PUT /enterprises/{id}/members/{idMember}/deactivated`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Deactivate a Member of an Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/enterprises/{{param:id}}/members/{{param:idMember}}/deactivated?value={{param:value}}&fields={{param:fields}}&organization_fields={{param:organization_fields}}&board_fields={{param:board_fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — ID of the enterprise to retrieve.
- `idMember` (path, string, required) — ID of the Member to deactive.
- `value` (query, string, required) — Determines whether the user is deactivated or not.
- `fields` (query, string, optional) — A comma separated list of any valid values that the [nested member field resource]() accepts.
- `organization_fields` (query, string, optional) — Any valid value that the nested organization resource accepts.
- `board_fields` (query, string, optional) — Any valid value that the nested board resource accepts.

## Original description

Deactivate a Member of an Enterprise.

 NOTE: Deactivation is not possible for enterprises that have opted in to user management via AdminHub.
