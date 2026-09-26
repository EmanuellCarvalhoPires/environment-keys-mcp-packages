---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/operation
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_permitted_operations_for_a_smart_link_in_the_cont
title: "Confluence v2 - Get permitted operations for a Smart Link in the content tree"
kind: request
request: "[[Confluence v2 - Get permitted operations for a Smart Link in the content tree]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /embeds/{id}/operations · Get permitted operations for a Smart Link in the content tree. Returns the permitted operations on specific Smart Link in the content tree. Permissions required: Permission to view the Smart Link in the content tree and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the Smart Link in the content tree for which operations should be returned."
writes: false
expose: false
---
# confluence_get_permitted_operations_for_a_smart_link_in_the_cont

`GET /embeds/{id}/operations` — Get permitted operations for a Smart Link in the content tree

- Request: [[Confluence v2 - Get permitted operations for a Smart Link in the content tree]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
