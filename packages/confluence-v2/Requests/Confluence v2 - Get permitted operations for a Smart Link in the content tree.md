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
path: "/embeds/{id}/operations"
category: "Operation"
writes_data: false
tool_note: "[[confluence_get_permitted_operations_for_a_smart_link_in_the_cont]]"
---
# Confluence v2 - Get permitted operations for a Smart Link in the content tree

**Get permitted operations for a Smart Link in the content tree** — `GET /embeds/{id}/operations`

- Run by the tool [[confluence_get_permitted_operations_for_a_smart_link_in_the_cont]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/embeds/{{param:id}}/operations
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the Smart Link in the content tree for which operations should be returned.

## Original description

Returns the permitted operations on specific Smart Link in the content tree.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the Smart Link in the content tree and its corresponding space.
