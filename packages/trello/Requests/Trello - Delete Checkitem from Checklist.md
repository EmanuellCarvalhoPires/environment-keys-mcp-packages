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
path: "/checklists/{id}/checkItems/{idCheckItem}"
category: "Checklists"
writes_data: true
---
# Trello - Delete Checkitem from Checklist

**Delete Checkitem from Checklist** — `DELETE /checklists/{id}/checkItems/{idCheckItem}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete Checkitem from Checklist"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/checklists/{{param:id}}/checkItems/{{param:idCheckItem}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idCheckItem` (path, string, required) — Value of idCheckItem in the path.

## Original description

Remove an item from a checklist
