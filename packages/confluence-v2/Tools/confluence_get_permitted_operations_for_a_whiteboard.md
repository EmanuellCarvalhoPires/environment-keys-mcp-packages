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
tool: confluence_get_permitted_operations_for_a_whiteboard
title: "Confluence v2 - Get permitted operations for a whiteboard"
kind: request
request: "[[Confluence v2 - Get permitted operations for a whiteboard]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /whiteboards/{id}/operations · Get permitted operations for a whiteboard. Returns the permitted operations on specific whiteboard. Permissions required: Permission to view the whiteboard and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the whiteboard for which operations should be returned."
writes: false
expose: false
---
# confluence_get_permitted_operations_for_a_whiteboard

`GET /whiteboards/{id}/operations` — Get permitted operations for a whiteboard

- Request: [[Confluence v2 - Get permitted operations for a whiteboard]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
