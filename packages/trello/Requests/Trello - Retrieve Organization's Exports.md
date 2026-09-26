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
path: "/organizations/{id}/exports"
category: "Organizations"
writes_data: false
---
# Trello - Retrieve Organization's Exports

**Retrieve Organization's Exports** — `GET /organizations/{id}/exports`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Retrieve Organization's Exports"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/organizations/{{param:id}}/exports
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Retrieve the exports that exist for the given organization
