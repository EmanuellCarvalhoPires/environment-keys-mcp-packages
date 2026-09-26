---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-properties
  - api/operation/delete
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_delete_space_property_by_id
title: "Confluence v2 - Delete space property by id"
kind: request
request: "[[Confluence v2 - Delete space property by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · DELETE /spaces/{space-id}/properties/{property-id} · Delete space property by id. Deletes a space property by its id. Permissions required: Permission to access the Confluence site ('Can use' global permission) and 'Admin' permission for the space. Writes data: yes."
params:
  "space_id":
    type: string
    required: true
    description: "The ID of the space the property belongs to."
  "property_id":
    type: string
    required: true
    description: "The ID of the property to be deleted."
writes: true
expose: false
---
# confluence_delete_space_property_by_id

`DELETE /spaces/{space-id}/properties/{property-id}` — Delete space property by id

- Request: [[Confluence v2 - Delete space property by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
