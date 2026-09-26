---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/labels
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/labels/{id}"
category: "Labels"
writes_data: true
---
# Trello - Update a Label

**Update a Label** — `PUT /labels/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a Label"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/labels/{{param:id}}?name={{param:name}}&color={{param:color}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `name` (query, string, optional) — The new name for the label
- `color` (query, string, optional) — The new color for the label. See: fields for color options

## Original description

Update a label by ID.
