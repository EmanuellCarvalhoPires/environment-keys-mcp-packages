---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/classification-level
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_database_classification_level
title: "Confluence v2 - Get database classification level"
kind: request
request: "[[Confluence v2 - Get database classification level]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /databases/{id}/classification-level · Get database classification level. Returns the classification level for a specific database. Permissions required: 'Permission to access the Confluence site ('Can use' global permission) and permission to view the database. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the database for which classification level should be returned."
writes: false
expose: false
---
# confluence_get_database_classification_level

`GET /databases/{id}/classification-level` — Get database classification level

- Request: [[Confluence v2 - Get database classification level]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
