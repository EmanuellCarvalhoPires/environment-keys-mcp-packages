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
path: "/organizations/{id}/memberships/{idMembership}"
category: "Organizations"
writes_data: false
---
# Trello - Get a Membership of an Organization

**Get a Membership of an Organization** — `GET /organizations/{id}/memberships/{idMembership}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Membership of an Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/organizations/{{param:id}}/memberships/{{param:idMembership}}?member={{param:member}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization
- `idMembership` (path, string, required) — The ID of the membership to load
- `member` (query, string, optional) — Whether to include the Member object in the response

## Original description

Get a single Membership for an Organization
