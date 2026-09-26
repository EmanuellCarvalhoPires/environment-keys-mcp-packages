---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/lists
  - api/operation/action
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/lists/{id}/archiveAllCards"
category: "Lists"
writes_data: true
---
# Trello - Archive all Cards in List

**Archive all Cards in List** — `POST /lists/{id}/archiveAllCards`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Archive all Cards in List"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/lists/{{param:id}}/archiveAllCards
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the list

## Original description

Archive all cards in a list
