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
tool: confluence_get_permitted_operations_for_space
title: "Confluence v2 - Get permitted operations for space"
kind: request
request: "[[Confluence v2 - Get permitted operations for space]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /spaces/{id}/operations · Get permitted operations for space. Returns the permitted operations on specific space. Permissions required: Permission to view the corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the space for which operations should be returned."
writes: false
expose: false
---
# confluence_get_permitted_operations_for_space

`GET /spaces/{id}/operations` — Get permitted operations for space

- Request: [[Confluence v2 - Get permitted operations for space]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
