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
path: "/actions/{idAction}/reactions/{id}"
category: "Actions"
writes_data: false
---
# Trello - Get Action's Reaction

**Get Action's Reaction** — `GET /actions/{idAction}/reactions/{id}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Action's Reaction"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/actions/{{param:idAction}}/reactions/{{param:id}}?member={{param:member}}&emoji={{param:emoji}}
Authorization: {{service.auth_token}}
```

## Parameters

- `idAction` (path, string, required) — Value of idAction in the path.
- `id` (path, string, required) — Value of id in the path.
- `member` (query, string, optional) — Whether to load the member as a nested resource. See Members Nested Resource
- `emoji` (query, string, optional) — Whether to load the emoji as a nested resource.

## Original description

Get information for a reaction
