---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/organizations
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/organizations/{id}/tags"
category: "Organizations"
writes_data: true
---
# Trello - Create a Tag in Organization

**Create a Tag in Organization** — `POST /organizations/{id}/tags`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a Tag in Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/organizations/{{param:id}}/tags
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Create a Tag in an Organization
