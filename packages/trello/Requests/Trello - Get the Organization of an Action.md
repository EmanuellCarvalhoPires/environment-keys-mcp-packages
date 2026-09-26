---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/actions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/actions/{id}/organization"
category: "Actions"
writes_data: false
---
# Trello - Get the Organization of an Action

**Get the Organization of an Action** — `GET /actions/{id}/organization`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get the Organization of an Action"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/actions/{{param:id}}/organization?fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the action
- `fields` (query, string, optional) — all or a comma-separated list of organization fields

## Original description

Get the Organization of an Action
