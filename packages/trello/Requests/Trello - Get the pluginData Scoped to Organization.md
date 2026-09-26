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
path: "/organizations/{id}/pluginData"
category: "Organizations"
writes_data: false
---
# Trello - Get the pluginData Scoped to Organization

**Get the pluginData Scoped to Organization** — `GET /organizations/{id}/pluginData`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get the pluginData Scoped to Organization"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/organizations/{{param:id}}/pluginData
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization

## Original description

Get organization scoped pluginData on this Workspace
