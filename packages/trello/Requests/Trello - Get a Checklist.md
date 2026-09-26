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
path: "/checklists/{id}"
category: "Checklists"
writes_data: false
---
# Trello - Get a Checklist

**Get a Checklist** — `GET /checklists/{id}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Checklist"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/checklists/{{param:id}}?cards={{param:cards}}&checkItems={{param:checkItems}}&checkItem_fields={{param:checkItem_fields}}&fields={{param:fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `cards` (query, string, optional) — Valid values: all, closed, none, open, visible. Cards is a nested resource. The additional query params available are documented at Cards Nested Resource.
- `checkItems` (query, string, optional) — The check items on the list to return. One of: all, none.
- `checkItem_fields` (query, string, optional) — The fields on the checkItem to return if checkItems are being returned. all or a comma-separated list of: name, nameData, pos, state, type, due, dueReminder, idMember
- `fields` (query, string, optional) — all or a comma-separated list of checklist fields

