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
path: "/checklists/{id}/{field}"
category: "Checklists"
writes_data: false
---
# Trello - Get field on a Checklist

**Get field on a Checklist** — `GET /checklists/{id}/{field}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get field on a Checklist"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/checklists/{{param:id}}/{{param:field}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `field` (path, string, required) — Value of field in the path.

