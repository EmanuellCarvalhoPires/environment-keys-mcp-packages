---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/whiteboard
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_delete_whiteboard
title: "Confluence v2 - Delete whiteboard"
kind: request
request: "[[Confluence v2 - Delete whiteboard]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /whiteboards/{id} · Delete whiteboard. Delete a whiteboard by id. Deleting a whiteboard moves the whiteboard to the trash, where it can be restored later Permissions required: Permission to view the whiteboard and its corresponding space. Permission to delete whiteboards in the space. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the whiteboard to be deleted."
writes: true
expose: false
---
# confluence_delete_whiteboard

`DELETE /whiteboards/{id}` — Delete whiteboard

- Request: [[Confluence v2 - Delete whiteboard]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
