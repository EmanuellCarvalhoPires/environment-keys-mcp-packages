---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/checklists
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/checklists"
category: "Checklists"
writes_data: true
---
# Trello - Create a Checklist

**Create a Checklist** — `POST /checklists`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create a Checklist"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/checklists?idCard={{param:idCard}}&name={{param:name}}&pos={{param:pos}}&idChecklistSource={{param:idChecklistSource}}
Authorization: {{service.auth_token}}
```

## Parameters

- `idCard` (query, string, required) — The ID of the Card that the checklist should be added to.
- `name` (query, string, optional) — The name of the checklist. Should be a string of length 1 to 16384.
- `pos` (query, string, optional) — The position of the checklist on the card. One of: top, bottom, or a positive number.
- `idChecklistSource` (query, string, optional) — The ID of a checklist to copy into the new checklist.

