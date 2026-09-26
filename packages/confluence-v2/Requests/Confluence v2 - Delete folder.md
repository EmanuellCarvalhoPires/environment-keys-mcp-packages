---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/folder
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: DELETE
path: "/folders/{id}"
category: "Folder"
writes_data: true
tool_note: "[[confluence_delete_folder]]"
---
# Confluence v2 - Delete folder

**Delete folder** — `DELETE /folders/{id}`

- Run by the tool [[confluence_delete_folder]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
DELETE {{service.url}}/wiki/api/v2/folders/{{param:id}}
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the folder to be deleted.

## Original description

Delete a folder by id.

Deleting a folder moves the folder to the trash, where it can be restored later

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to view the folder and its corresponding space.
Permission to delete folders in the space.
