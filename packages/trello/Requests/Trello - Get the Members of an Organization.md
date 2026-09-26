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
path: "/organizations/{id}/members"
category: "Organizations"
writes_data: false
---
# Trello - Get the Members of an Organization

**Get the Members of an Organization** — `GET /organizations/{id}/members`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get the Members of an Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/organizations/{{param:id}}/members
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or name of the Organization

## Original description

List the members in a Workspace
