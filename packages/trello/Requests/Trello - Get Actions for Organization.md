---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/organizations
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/organizations/{id}/actions"
category: "Organizations"
writes_data: false
---
# Trello - Get Actions for Organization

**Get Actions for Organization** — `GET /organizations/{id}/actions`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Actions for Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/organizations/{{param:id}}/actions
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization

## Original description

List the actions on a Workspace
