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
path: "/organizations/{id}/logo"
category: "Organizations"
writes_data: true
---
# Trello - Delete Logo for Organization

**Delete Logo for Organization** — `DELETE /organizations/{id}/logo`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete Logo for Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/organizations/{{param:id}}/logo
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization

## Original description

Delete a the logo from a Workspace
