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
tool: confluence_get_permitted_operations_for_a_database
title: "Confluence v2 - Get permitted operations for a database"
kind: request
request: "[[Confluence v2 - Get permitted operations for a database]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /databases/{id}/operations · Get permitted operations for a database. Returns the permitted operations on specific database. Permissions required: Permission to view the database and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the database for which operations should be returned."
writes: false
expose: false
---
# confluence_get_permitted_operations_for_a_database

`GET /databases/{id}/operations` — Get permitted operations for a database

- Request: [[Confluence v2 - Get permitted operations for a database]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
