---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/customfields
  - api/operation/list
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/customFields/{id}/options"
category: "CustomFields"
writes_data: false
---
# Trello - Get Options of Custom Field drop down

**Get Options of Custom Field drop down** — `GET /customFields/{id}/options`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Options of Custom Field drop down"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/customFields/{{param:id}}/options
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Get the options of a drop down Custom Field
