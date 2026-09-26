---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/database
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_delete_database
title: "Confluence v2 - Delete database"
kind: request
request: "[[Confluence v2 - Delete database]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /databases/{id} · Delete database. Delete a database by id. Deleting a database moves the database to the trash, where it can be restored later Permissions required: Permission to view the database and its corresponding space. Permission to delete databases in the space. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the database to be deleted."
writes: true
expose: false
---
# confluence_delete_database

`DELETE /databases/{id}` — Delete database

- Request: [[Confluence v2 - Delete database]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
