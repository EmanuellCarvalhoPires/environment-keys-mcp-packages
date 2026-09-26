---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/whiteboard
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: DELETE
path: "/whiteboards/{id}"
category: "Whiteboard"
writes_data: true
tool_note: "[[confluence_delete_whiteboard]]"
---
# Confluence v2 - Delete whiteboard

**Delete whiteboard** — `DELETE /whiteboards/{id}`

- Run by the tool [[confluence_delete_whiteboard]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
DELETE {{service.url}}/wiki/api/v2/whiteboards/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the whiteboard to be deleted.

## Original description

Delete a whiteboard by id.

Deleting a whiteboard moves the whiteboard to the trash, where it can be restored later

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the whiteboard and its corresponding space.
Permission to delete whiteboards in the space.
