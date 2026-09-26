---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/lists
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/lists/{id}/{field}"
category: "Lists"
writes_data: true
---
# Trello - Update a field on a List

**Update a field on a List** — `PUT /lists/{id}/{field}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a field on a List"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/lists/{{param:id}}/{{param:field}}?value={{param:value}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the list
- `field` (path, string, required) — The field on the List to be updated
- `value` (query, string, optional) — The new value for the field

## Original description

Rename a list
