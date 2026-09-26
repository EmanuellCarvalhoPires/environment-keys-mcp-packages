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
tool: confluence_get_permitted_operations_for_a_folder
title: "Confluence v2 - Get permitted operations for a folder"
kind: request
request: "[[Confluence v2 - Get permitted operations for a folder]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /folders/{id}/operations · Get permitted operations for a folder. Returns the permitted operations on specific folder. Permissions required: Permission to view the folder and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the folder for which operations should be returned."
writes: false
expose: false
---
# confluence_get_permitted_operations_for_a_folder

`GET /folders/{id}/operations` — Get permitted operations for a folder

- Request: [[Confluence v2 - Get permitted operations for a folder]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
