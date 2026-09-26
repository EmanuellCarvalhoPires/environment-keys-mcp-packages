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
path: "/plugins/{id}/compliance/memberPrivacy"
category: "Plugins"
writes_data: false
---
# Trello - Get Plugin's Member privacy compliance

**Get Plugin's Member privacy compliance** — `GET /plugins/{id}/compliance/memberPrivacy`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Plugin's Member privacy compliance"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/plugins/{{param:id}}/compliance/memberPrivacy
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the Power-Up

