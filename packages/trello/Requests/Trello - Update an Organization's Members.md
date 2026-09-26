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
path: "/organizations/{id}/members"
category: "Organizations"
writes_data: true
---
# Trello - Update an Organization's Members

**Update an Organization's Members** — `PUT /organizations/{id}/members`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update an Organization's Members"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/organizations/{{param:id}}/members?email={{param:email}}&fullName={{param:fullName}}&type={{param:type}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization
- `email` (query, string, required) — An email address
- `fullName` (query, string, required) — Name for the member, at least 1 character not beginning or ending with a space
- `type` (query, string, optional) — One of: admin, normal

