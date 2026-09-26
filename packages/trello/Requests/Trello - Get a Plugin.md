---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/plugins
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/plugins/{id}/"
category: "Plugins"
writes_data: false
---
# Trello - Get a Plugin

**Get a Plugin** — `GET /plugins/{id}/`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Plugin"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/plugins/{{param:id}}/
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization

## Original description

Get plugins
