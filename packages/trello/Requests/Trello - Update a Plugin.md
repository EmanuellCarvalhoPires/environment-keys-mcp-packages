---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/plugins
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/plugins/{id}/"
category: "Plugins"
writes_data: true
---
# Trello - Update a Plugin

**Update a Plugin** — `PUT /plugins/{id}/`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a Plugin"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/plugins/{{param:id}}/
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization

## Original description

Update a Plugin
