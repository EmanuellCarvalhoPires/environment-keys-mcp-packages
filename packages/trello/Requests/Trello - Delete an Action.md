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
path: "/actions/{id}"
category: "Actions"
writes_data: true
---
# Trello - Delete an Action

**Delete an Action** — `DELETE /actions/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete an Action"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/actions/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Delete a specific action. Only comment actions can be deleted.
