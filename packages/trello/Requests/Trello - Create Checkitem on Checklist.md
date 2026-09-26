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
path: "/checklists/{id}/checkItems"
category: "Checklists"
writes_data: true
---
# Trello - Create Checkitem on Checklist

**Create Checkitem on Checklist** — `POST /checklists/{id}/checkItems`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Create Checkitem on Checklist"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/checklists/{{param:id}}/checkItems?name={{param:name}}&pos={{param:pos}}&checked={{param:checked}}&due={{param:due}}&dueReminder={{param:dueReminder}}&idMember={{param:idMember}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `name` (query, string, required) — The name of the new check item on the checklist. Should be a string of length 1 to 16384.
- `pos` (query, string, optional) — The position of the check item in the checklist. One of: top, bottom, or a positive number.
- `checked` (query, string, optional) — Determines whether the check item is already checked when created.
- `due` (query, string, optional) — A due date for the checkitem
- `dueReminder` (query, string, optional) — A dueReminder for the due date on the checkitem
- `idMember` (query, string, optional) — An ID of a member resource.

