---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/actions
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/actions/{idAction}/reactions/{id}"
category: "Actions"
writes_data: true
---
# Trello - Delete Action's Reaction

**Delete Action's Reaction** — `DELETE /actions/{idAction}/reactions/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete Action's Reaction"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/actions/{{param:idAction}}/reactions/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `idAction` (path, string, required) — Value of idAction in the path.
- `id` (path, string, required) — Value of id in the path.

## Original description

Deletes a reaction
