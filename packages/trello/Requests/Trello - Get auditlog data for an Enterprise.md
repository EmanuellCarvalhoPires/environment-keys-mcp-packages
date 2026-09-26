---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/enterprises
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/enterprises/{id}/auditlog"
category: "Enterprises"
writes_data: false
---
# Trello - Get auditlog data for an Enterprise

**Get auditlog data for an Enterprise** — `GET /enterprises/{id}/auditlog`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get auditlog data for an Enterprise"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/enterprises/{{param:id}}/auditlog
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — ID of the enterprise to retrieve.

## Original description

Returns an array of Actions related to the Enterprise object. Used for populating data sent to Google Sheets from an Enterprise's audit log page: https://trello.com/e/{enterprise_name}/admin/auditlog. An Enterprise admin token is required for this route. 

 NOTE: For enterprises that have opted in to user management via AdminHub, the auditlog will will contain actions taken in AdminHub, but may not contain the source for those actions.
