---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/customfields
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/customFields/{id}"
category: "CustomFields"
writes_data: false
---
# Trello - Get a Custom Field

**Get a Custom Field** — `GET /customFields/{id}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get a Custom Field"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/customFields/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

