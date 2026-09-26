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
tool: confluence_get_permitted_operations_for_attachment
title: "Confluence v2 - Get permitted operations for attachment"
kind: request
request: "[[Confluence v2 - Get permitted operations for attachment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /attachments/{id}/operations · Get permitted operations for attachment. Returns the permitted operations on specific attachment. Permissions required: Permission to view the parent content of the attachment and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the attachment for which operations should be returned."
writes: false
expose: false
---
# confluence_get_permitted_operations_for_attachment

`GET /attachments/{id}/operations` — Get permitted operations for attachment

- Request: [[Confluence v2 - Get permitted operations for attachment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
