---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/organizations
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/organizations/{id}/newBillableGuests/{idBoard}"
category: "Organizations"
writes_data: false
---
# Trello - Get Organizations new billable guests

**Get Organizations new billable guests** — `GET /organizations/{id}/newBillableGuests/{idBoard}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Organizations new billable guests"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/organizations/{{param:id}}/newBillableGuests/{{param:idBoard}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID or name of the organization
- `idBoard` (path, string, required) — The ID of the board to check for new billable guests.

## Original description

Used to check whether the given board has new billable guests on it.
