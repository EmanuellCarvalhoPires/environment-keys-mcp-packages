---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/checklists
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/checklists/{id}"
category: "Checklists"
writes_data: true
---
# Trello - Delete a Checklist

**Delete a Checklist** — `DELETE /checklists/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete a Checklist"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/checklists/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Delete a checklist
