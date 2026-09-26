---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/checklists
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/checklists/{id}/checkItems"
category: "Checklists"
writes_data: false
---
# Trello - Get Checkitems on a Checklist

**Get Checkitems on a Checklist** — `GET /checklists/{id}/checkItems`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Checkitems on a Checklist"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/checklists/{{param:id}}/checkItems?filter={{param:filter}}&fields={{param:fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `filter` (query, string, optional) — One of: all, none.
- `fields` (query, string, optional) — One of: all, name, nameData, pos, state,type, due, dueReminder, idMember.

