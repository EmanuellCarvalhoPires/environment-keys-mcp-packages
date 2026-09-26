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
path: "/actions/{id}"
category: "Actions"
writes_data: true
---
# Trello - Update an Action

**Update an Action** — `PUT /actions/{id}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Update an Action"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
PUT {{service.url}}/actions/{{param:id}}?text={{param:text}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `text` (query, string, required) — The new text for the comment

## Original description

Update a specific Action. Only comment actions can be updated. Used to edit the content of a comment.
