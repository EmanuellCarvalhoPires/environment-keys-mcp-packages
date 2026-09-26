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
path: "/checklists/{id}/cards"
category: "Checklists"
writes_data: false
---
# Trello - Get the Card a Checklist is on

**Get the Card a Checklist is on** — `GET /checklists/{id}/cards`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get the Card a Checklist is on"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/checklists/{{param:id}}/cards
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — ID of a checklist.

