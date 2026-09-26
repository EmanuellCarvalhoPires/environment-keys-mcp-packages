---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/organizations
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/organizations/{id}/members/{idMember}/deactivated"
category: "Organizations"
writes_data: true
---
# Trello - Deactivate or reactivate a member of an Organization

**Deactivate or reactivate a member of an Organization** — `PUT /organizations/{id}/members/{idMember}/deactivated`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Deactivate or reactivate a member of an Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/organizations/{{param:id}}/members/{{param:idMember}}/deactivated?value={{param:value}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization
- `idMember` (path, string, required) — The ID or username of the member to update
- `value` (query, string, required) — Query parameter value.

## Original description

Deactivate or reactivate a member of a Workspace
