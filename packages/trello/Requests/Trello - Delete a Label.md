---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/labels
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/labels/{id}"
category: "Labels"
writes_data: true
---
# Trello - Delete a Label

**Delete a Label** — `DELETE /labels/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete a Label"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/labels/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Delete a label by ID.
