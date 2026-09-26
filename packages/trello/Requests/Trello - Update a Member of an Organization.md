---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/organizations
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/organizations/{id}/members/{idMember}"
category: "Organizations"
writes_data: true
---
# Trello - Update a Member of an Organization

**Update a Member of an Organization** — `PUT /organizations/{id}/members/{idMember}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a Member of an Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/organizations/{{param:id}}/members/{{param:idMember}}?type={{param:type}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization
- `idMember` (path, string, required) — The ID or username of the member to update
- `type` (query, string, required) — One of: admin, normal

## Original description

Add a member to a Workspace or update their member type.
