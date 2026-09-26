---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-properties
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_update_space_property_by_id
title: "Confluence v2 - Update space property by id"
kind: request
request: "[[Confluence v2 - Update space property by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · PUT /spaces/{space-id}/properties/{property-id} · Update space property by id. Update a space property by its id. Permissions required: Permission to access the Confluence site ('Can use' global permission) and 'Admin' permission for the space. Writes data: yes."
params:
  "space_id":
    type: string
    required: true
    description: "The ID of the space the property belongs to."
  "property_id":
    type: string
    required: true
    description: "The ID of the property to be updated."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_update_space_property_by_id

`PUT /spaces/{space-id}/properties/{property-id}` — Update space property by id

- Request: [[Confluence v2 - Update space property by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
