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
path: "/actions/{idAction}/reactions"
category: "Actions"
writes_data: false
---
# Trello - Get Action's Reactions

**Get Action's Reactions** — `GET /actions/{idAction}/reactions`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Action's Reactions"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/actions/{{param:idAction}}/reactions?member={{param:member}}&emoji={{param:emoji}}
Authorization: {{service.auth_token}}
```

## Parameters

- `idAction` (path, string, required) — Value of idAction in the path.
- `member` (query, string, optional) — Whether to load the member as a nested resource. See Members Nested Resource
- `emoji` (query, string, optional) — Whether to load the emoji as a nested resource.

## Original description

List reactions for an action
