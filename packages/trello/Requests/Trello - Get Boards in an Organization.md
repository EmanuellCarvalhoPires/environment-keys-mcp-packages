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
path: "/organizations/{id}/boards"
category: "Organizations"
writes_data: false
---
# Trello - Get Boards in an Organization

**Get Boards in an Organization** — `GET /organizations/{id}/boards`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Boards in an Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/organizations/{{param:id}}/boards?filter={{param:filter}}&fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization
- `filter` (query, string, optional) — all or a comma-separated list of: open, closed, members, organization, public
- `fields` (query, string, optional) — all or a comma-separated list of board fields

## Original description

List the boards in a Workspace
