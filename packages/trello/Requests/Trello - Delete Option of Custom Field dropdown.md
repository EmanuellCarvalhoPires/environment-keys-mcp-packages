---
tags:
  - api/request
  - api/service/trello
  - api/app/trello
  - api/resource/customfields
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Trello]]"
app: "Trello"
method: DELETE
path: "/customFields/{id}/options/{idCustomFieldOption}"
category: "CustomFields"
writes_data: true
---
# Trello - Delete Option of Custom Field dropdown

**Delete Option of Custom Field dropdown** — `DELETE /customFields/{id}/options/{idCustomFieldOption}`

- No dedicated tool: run it with `trello_request_write` passing `request:"Trello - Delete Option of Custom Field dropdown"`.
- Official documentation: https://developer.atlassian.com/cloud/trello/rest/

```http
DELETE {{service.url}}/customFields/{{param:id}}/options/{{param:idCustomFieldOption}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — Value of id in the path.
- `idCustomFieldOption` (path, string, required) — Value of idCustomFieldOption in the path.

## Original description

Delete an option from a Custom Field dropdown.
