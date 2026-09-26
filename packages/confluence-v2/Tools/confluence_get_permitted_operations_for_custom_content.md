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
tool: confluence_get_permitted_operations_for_custom_content
title: "Confluence v2 - Get permitted operations for custom content"
kind: request
request: "[[Confluence v2 - Get permitted operations for custom content]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /custom-content/{id}/operations · Get permitted operations for custom content. Returns the permitted operations on specific custom content. Permissions required: Permission to view the parent content of the custom content and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the custom content for which operations should be returned."
writes: false
expose: false
---
# confluence_get_permitted_operations_for_custom_content

`GET /custom-content/{id}/operations` — Get permitted operations for custom content

- Request: [[Confluence v2 - Get permitted operations for custom content]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
