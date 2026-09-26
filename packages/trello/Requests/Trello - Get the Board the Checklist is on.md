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
path: "/checklists/{id}/board"
category: "Checklists"
writes_data: false
---
# Trello - Get the Board the Checklist is on

**Get the Board the Checklist is on** — `GET /checklists/{id}/board`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get the Board the Checklist is on"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/checklists/{{param:id}}/board?fields={{param:fields}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — ID of a checklist.
- `fields` (query, string, optional) — all or a comma-separated list of board fields

