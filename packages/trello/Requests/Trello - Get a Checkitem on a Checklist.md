---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/checklists
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/checklists/{id}/checkItems/{idCheckItem}"
category: "Checklists"
writes_data: false
---
# Trello - Get a Checkitem on a Checklist

**Get a Checkitem on a Checklist** — `GET /checklists/{id}/checkItems/{idCheckItem}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Checkitem on a Checklist"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/checklists/{{param:id}}/checkItems/{{param:idCheckItem}}?fields={{param:fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idCheckItem` (path, string, required) — Value of idCheckItem in the path.
- `fields` (query, string, optional) — One of: all, name, nameData, pos, state, type, due, dueReminder, idMember,.

