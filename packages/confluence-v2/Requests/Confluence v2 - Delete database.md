---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/database
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: DELETE
path: "/databases/{id}"
category: "Database"
writes_data: true
tool_note: "[[confluence_delete_database]]"
---
# Confluence v2 - Delete database

**Delete database** — `DELETE /databases/{id}`

- Run by the tool [[confluence_delete_database]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
DELETE {{service.url}}/wiki/api/v2/databases/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the database to be deleted.

## Original description

Delete a database by id.

Deleting a database moves the database to the trash, where it can be restored later

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the database and its corresponding space.
Permission to delete databases in the space.
