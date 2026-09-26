---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/actions
  - api/operation/update
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: PUT
path: "/actions/{id}/text"
category: "Actions"
writes_data: true
---
# Trello - Update a Comment Action

**Update a Comment Action** — `PUT /actions/{id}/text`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update a Comment Action"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/actions/{{param:id}}/text?value={{param:value}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the action to update
- `value` (query, string, required) — The new text for the comment

## Original description

Update a comment action
