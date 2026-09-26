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
path: "/lists/{id}"
category: "Lists"
writes_data: true
---
# Trello - Update a List

**Update a List** — `PUT /lists/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a List"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/lists/{{param:id}}?name={{param:name}}&closed={{param:closed}}&idBoard={{param:idBoard}}&pos={{param:pos}}&subscribed={{param:subscribed}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `name` (query, string, optional) — New name for the list
- `closed` (query, string, optional) — Whether the list should be closed (archived)
- `idBoard` (query, string, optional) — ID of a board the list should be moved to
- `pos` (query, string, optional) — New position for the list: top, bottom, or a positive floating point number
- `subscribed` (query, string, optional) — Whether the active member is subscribed to this list

## Original description

Update the properties of a List
