---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/organizations
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/organizations/{id}/members/{idMember}"
category: "Organizations"
writes_data: true
---
# Trello - Remove a Member from an Organization

**Remove a Member from an Organization** — `DELETE /organizations/{id}/members/{idMember}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Remove a Member from an Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/organizations/{{param:id}}/members/{{param:idMember}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization
- `idMember` (path, string, required) — The ID of the Member to remove from the Workspace

## Original description

Remove a member from a Workspace
