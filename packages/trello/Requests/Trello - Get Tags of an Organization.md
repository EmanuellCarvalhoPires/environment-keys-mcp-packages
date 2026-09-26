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
path: "/organizations/{id}/tags"
category: "Organizations"
writes_data: false
---
# Trello - Get Tags of an Organization

**Get Tags of an Organization** — `GET /organizations/{id}/tags`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Tags of an Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/organizations/{{param:id}}/tags
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

List the organization's collections
