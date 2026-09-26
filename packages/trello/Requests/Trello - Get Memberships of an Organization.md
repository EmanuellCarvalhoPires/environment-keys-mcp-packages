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
path: "/organizations/{id}/memberships"
category: "Organizations"
writes_data: false
---
# Trello - Get Memberships of an Organization

**Get Memberships of an Organization** — `GET /organizations/{id}/memberships`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Memberships of an Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/organizations/{{param:id}}/memberships?filter={{param:filter}}&member={{param:member}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization
- `filter` (query, string, optional) — all or a comma-separated list of: active, admin, deactivated, me, normal
- `member` (query, string, optional) — Whether to include the Member objects with the Memberships

## Original description

List the memberships of a Workspace
