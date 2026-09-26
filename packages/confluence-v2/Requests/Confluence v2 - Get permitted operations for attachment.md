---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/operation
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: GET
path: "/attachments/{id}/operations"
category: "Operation"
writes_data: false
tool_note: "[[confluence_get_permitted_operations_for_attachment]]"
---
# Confluence v2 - Get permitted operations for attachment

**Get permitted operations for attachment** — `GET /attachments/{id}/operations`

- Run by the tool [[confluence_get_permitted_operations_for_attachment]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/attachments/{{param:id}}/operations
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the attachment for which operations should be returned.

## Original description

Returns the permitted operations on specific attachment.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the parent content of the attachment and its corresponding space.
