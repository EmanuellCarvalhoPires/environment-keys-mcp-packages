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
path: "/organizations/{id}"
category: "Organizations"
writes_data: true
---
# Trello - Delete an Organization

**Delete an Organization** — `DELETE /organizations/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete an Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/organizations/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Delete an Organization
