---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/checklists
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/checklists/{id}/{field}"
category: "Checklists"
writes_data: true
---
# Trello - Update field on a Checklist

**Update field on a Checklist** — `PUT /checklists/{id}/{field}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update field on a Checklist"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/checklists/{{param:id}}/{{param:field}}?value={{param:value}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `field` (path, string, required) — Value of field in the path.
- `value` (query, string, required) — The value to change the checklist name to. Should be a string of length 1 to 16384.

