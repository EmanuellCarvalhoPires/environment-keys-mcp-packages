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
path: "/organizations/{id}/members/{idMember}/all"
category: "Organizations"
writes_data: true
---
# Trello - Remove a Member from an Organization and all Organization Boards

**Remove a Member from an Organization and all Organization Boards** — `DELETE /organizations/{id}/members/{idMember}/all`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Remove a Member from an Organization and all Organization Boards"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/organizations/{{param:id}}/members/{{param:idMember}}/all
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization
- `idMember` (path, string, required) — The ID of the member to remove from the Workspace

## Original description

Remove a member from a Workspace and from all Workspace boards
