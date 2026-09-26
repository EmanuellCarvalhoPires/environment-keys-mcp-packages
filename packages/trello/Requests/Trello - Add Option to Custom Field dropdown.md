---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/customfields
  - api/operation/create
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: POST
path: "/customFields/{id}/options"
category: "CustomFields"
writes_data: true
---
# Trello - Add Option to Custom Field dropdown

**Add Option to Custom Field dropdown** — `POST /customFields/{id}/options`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Add Option to Custom Field dropdown"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
POST {{service.url}}/customFields/{{param:id}}/options
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Add an option to a dropdown Custom Field
