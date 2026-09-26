---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/smart-link
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_delete_smart_link_in_the_content_tree
title: "Confluence v2 - Delete Smart Link in the content tree"
kind: request
request: "[[Confluence v2 - Delete Smart Link in the content tree]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /embeds/{id} · Delete Smart Link in the content tree. Delete a Smart Link in the content tree by id. Deleting a Smart Link in the content tree moves the Smart Link to the trash, where it can be restored later Permissions required: Permission to view the Smart Link in the content tree and its corresponding space. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the Smart Link in the content tree to be deleted."
writes: true
expose: false
---
# confluence_delete_smart_link_in_the_content_tree

`DELETE /embeds/{id}` — Delete Smart Link in the content tree

- Request: [[Confluence v2 - Delete Smart Link in the content tree]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
