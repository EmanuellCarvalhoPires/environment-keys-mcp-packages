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
tool: confluence_get_permitted_operations_for_page
title: "Confluence v2 - Get permitted operations for page"
kind: request
request: "[[Confluence v2 - Get permitted operations for page]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /pages/{id}/operations · Get permitted operations for page. Returns the permitted operations on specific page. Permissions required: Permission to view the parent content of the page and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the page for which operations should be returned."
writes: false
expose: false
---
# confluence_get_permitted_operations_for_page

`GET /pages/{id}/operations` — Get permitted operations for page

- Request: [[Confluence v2 - Get permitted operations for page]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
