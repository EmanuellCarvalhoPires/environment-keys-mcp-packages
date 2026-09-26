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
path: "/lists/{id}/closed"
category: "Lists"
writes_data: true
---
# Trello - Archive or unarchive a list

**Archive or unarchive a list** — `PUT /lists/{id}/closed`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Archive or unarchive a list"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/lists/{{param:id}}/closed?value={{param:value}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the list
- `value` (query, string, optional) — Set to true to close (archive) the list

## Original description

Archive or unarchive a list
