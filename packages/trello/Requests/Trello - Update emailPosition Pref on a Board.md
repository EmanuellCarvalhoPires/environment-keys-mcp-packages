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
path: "/boards/{id}/myPrefs/emailPosition"
category: "Boards"
writes_data: true
---
# Trello - Update emailPosition Pref on a Board

**Update emailPosition Pref on a Board** — `PUT /boards/{id}/myPrefs/emailPosition`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update emailPosition Pref on a Board"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/boards/{{param:id}}/myPrefs/emailPosition?value={{param:value}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The id of the board to update
- `value` (query, string, required) — Valid values: bottom, top. Determines the position of the email address.

## Original description

Update emailPosition Pref on a Board
