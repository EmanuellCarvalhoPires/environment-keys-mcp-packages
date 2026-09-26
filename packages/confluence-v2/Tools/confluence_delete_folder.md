---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/folder
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_delete_folder
title: "Confluence v2 - Delete folder"
kind: request
request: "[[Confluence v2 - Delete folder]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /folders/{id} · Delete folder. Delete a folder by id. Deleting a folder moves the folder to the trash, where it can be restored later Permissions required: Permission to view the folder and its corresponding space. Permission to delete folders in the space. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the folder to be deleted."
writes: true
expose: false
---
# confluence_delete_folder

`DELETE /folders/{id}` — Delete folder

- Request: [[Confluence v2 - Delete folder]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
