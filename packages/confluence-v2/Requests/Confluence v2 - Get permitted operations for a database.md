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
path: "/databases/{id}/operations"
category: "Operation"
writes_data: false
tool_note: "[[confluence_get_permitted_operations_for_a_database]]"
---
# Confluence v2 - Get permitted operations for a database

**Get permitted operations for a database** — `GET /databases/{id}/operations`

- Run by the tool [[confluence_get_permitted_operations_for_a_database]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
GET {{service.url}}/wiki/api/v2/databases/{{param:id}}/operations
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the database for which operations should be returned.

## Original description

Returns the permitted operations on specific database.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the database and its corresponding space.
