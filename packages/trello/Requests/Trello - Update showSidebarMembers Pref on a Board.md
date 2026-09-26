---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/boards
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/boards/{id}/myPrefs/showSidebarMembers"
category: "Boards"
writes_data: true
---
# Trello - Update showSidebarMembers Pref on a Board

**Update showSidebarMembers Pref on a Board** — `PUT /boards/{id}/myPrefs/showSidebarMembers`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update showSidebarMembers Pref on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/boards/{{param:id}}/myPrefs/showSidebarMembers?value={{param:value}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The id of the board to update
- `value` (query, string, required) — Determines whether to show members of the board in the sidebar.

