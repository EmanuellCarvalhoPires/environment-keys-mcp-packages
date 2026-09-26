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
path: "/actions/{idAction}/reactionsSummary"
category: "Actions"
writes_data: false
---
# Trello - List Action's summary of Reactions

**List Action's summary of Reactions** — `GET /actions/{idAction}/reactionsSummary`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - List Action's summary of Reactions"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/actions/{{param:idAction}}/reactionsSummary
Authorization: {{service.auth_token}}
```

## Parameters

- `idAction` (path, string, required) — The ID of the action

## Original description

List a summary of all reactions for an action
