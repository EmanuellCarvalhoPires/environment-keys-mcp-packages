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
path: "/labels/{id}/{field}"
category: "Labels"
writes_data: true
---
# Trello - Update a field on a label

**Update a field on a label** — `PUT /labels/{id}/{field}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a field on a label"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/labels/{{param:id}}/{{param:field}}?value={{param:value}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The id of the label
- `field` (path, string, required) — The field on the Label to update.
- `value` (query, string, required) — The new value for the field.

## Original description

Update a field on a label.
