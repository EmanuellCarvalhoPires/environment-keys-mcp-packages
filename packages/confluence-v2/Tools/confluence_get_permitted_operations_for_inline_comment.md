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
tool: confluence_get_permitted_operations_for_inline_comment
title: "Confluence v2 - Get permitted operations for inline comment"
kind: request
request: "[[Confluence v2 - Get permitted operations for inline comment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /inline-comments/{id}/operations · Get permitted operations for inline comment. Returns the permitted operations on specific inline comment. Permissions required: Permission to view the parent content of the inline comment and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the inline comment for which operations should be returned."
writes: false
expose: false
---
# confluence_get_permitted_operations_for_inline_comment

`GET /inline-comments/{id}/operations` — Get permitted operations for inline comment

- Request: [[Confluence v2 - Get permitted operations for inline comment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
