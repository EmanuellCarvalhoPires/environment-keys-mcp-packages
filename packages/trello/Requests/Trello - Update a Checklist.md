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
path: "/checklists/{id}"
category: "Checklists"
writes_data: true
---
# Trello - Update a Checklist

**Update a Checklist** — `PUT /checklists/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a Checklist"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/checklists/{{param:id}}?name={{param:name}}&pos={{param:pos}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `name` (query, string, optional) — Name of the new checklist being created. Should be length of 1 to 16384.
- `pos` (query, string, optional) — Determines the position of the checklist on the card. One of: top, bottom, or a positive number.

## Original description

Update an existing checklist.
