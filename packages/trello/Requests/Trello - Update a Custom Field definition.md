---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/customfields
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/customFields/{id}"
category: "CustomFields"
writes_data: true
---
# Trello - Update a Custom Field definition

**Update a Custom Field definition** — `PUT /customFields/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a Custom Field definition"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/customFields/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update a Custom Field definition.
