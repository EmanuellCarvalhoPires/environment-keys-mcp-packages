---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/organizations
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/organizations/{id}/{field}"
category: "Organizations"
writes_data: false
---
# Trello - Get field on Organization

**Get field on Organization** — `GET /organizations/{id}/{field}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get field on Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/organizations/{{param:id}}/{{param:field}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization
- `field` (path, string, required) — An organization field

