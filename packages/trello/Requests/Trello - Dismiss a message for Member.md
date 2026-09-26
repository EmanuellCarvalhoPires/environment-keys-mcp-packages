---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/members
  - api/operation/action
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/members/{id}/oneTimeMessagesDismissed"
category: "Members"
writes_data: true
---
# Trello - Dismiss a message for Member

**Dismiss a message for Member** — `POST /members/{id}/oneTimeMessagesDismissed`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Dismiss a message for Member"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/members/{{param:id}}/oneTimeMessagesDismissed?value={{param:value}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID or username of the member
- `value` (query, string, required) — The message to dismiss

## Original description

Dismiss a message
