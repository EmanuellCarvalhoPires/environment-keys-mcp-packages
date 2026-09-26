---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/customfields
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/customFields/{id}"
category: "CustomFields"
writes_data: true
---
# Trello - Delete a Custom Field definition

**Delete a Custom Field definition** — `DELETE /customFields/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete a Custom Field definition"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/customFields/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Delete a Custom Field from a board.
