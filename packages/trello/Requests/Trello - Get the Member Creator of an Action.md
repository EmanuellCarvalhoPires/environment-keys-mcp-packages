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
path: "/actions/{id}/memberCreator"
category: "Actions"
writes_data: false
---
# Trello - Get the Member Creator of an Action

**Get the Member Creator of an Action** — `GET /actions/{id}/memberCreator`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get the Member Creator of an Action"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/actions/{{param:id}}/memberCreator?fields={{param:fields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the Action
- `fields` (query, string, optional) — all or a comma-separated list of member fields

## Original description

Get the Member who created the Action

*Note: An action can live on a board or a workspace, so accessing it needs `read:board:trello` or `read:organization:trello`.*
