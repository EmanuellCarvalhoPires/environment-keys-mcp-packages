---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/actions
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/actions/{id}/{field}"
category: "Actions"
writes_data: false
---
# Trello - Get a specific field on an Action

**Get a specific field on an Action** — `GET /actions/{id}/{field}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a specific field on an Action"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/actions/{{param:id}}/{{param:field}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the Action
- `field` (path, string, required) — An action field

## Original description

Get a specific property of an action

*Note: An action can live on a board or a workspace, so accessing it needs `read:board:trello` or `read:organization:trello`.*
