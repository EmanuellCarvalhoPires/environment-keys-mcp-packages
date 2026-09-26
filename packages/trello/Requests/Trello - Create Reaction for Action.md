---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/actions
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/actions/{idAction}/reactions"
category: "Actions"
writes_data: true
---
# Trello - Create Reaction for Action

**Create Reaction for Action** — `POST /actions/{idAction}/reactions`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create Reaction for Action"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/actions/{{param:idAction}}/reactions
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `idAction` (path, string, required) — Value of idAction in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Adds a new reaction to an action
