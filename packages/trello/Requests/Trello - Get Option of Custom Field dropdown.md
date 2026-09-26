---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/customfields
  - api/operation/get
  - api/effect/read
up: "[[MCP - Trello]]"
app: "Trello"
method: GET
path: "/customFields/{id}/options/{idCustomFieldOption}"
category: "CustomFields"
writes_data: false
---
# Trello - Get Option of Custom Field dropdown

**Get Option of Custom Field dropdown** — `GET /customFields/{id}/options/{idCustomFieldOption}`

- No dedicated tool: run it with `trello_request_read` passing `request:"Trello - Get Option of Custom Field dropdown"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
GET {{service.url}}/customFields/{{param:id}}/options/{{param:idCustomFieldOption}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idCustomFieldOption` (path, string, required) — Value of idCustomFieldOption in the path.

## Original description

Retrieve a specific, existing Option on a given dropdown-type Custom Field
