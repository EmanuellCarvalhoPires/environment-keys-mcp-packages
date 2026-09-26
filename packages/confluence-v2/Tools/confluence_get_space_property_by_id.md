---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-properties
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_space_property_by_id
title: "Confluence v2 - Get space property by id"
kind: request
request: "[[Confluence v2 - Get space property by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /spaces/{space-id}/properties/{property-id} · Get space property by id. Retrieve a space property by its id. Permissions required: Permission to access the Confluence site ('Can use' global permission) and 'View' permission for the space. Writes data: no."
params:
  "space_id":
    type: string
    required: true
    description: "The ID of the space the property belongs to."
  "property_id":
    type: string
    required: true
    description: "The ID of the property to be retrieved."
writes: false
expose: false
---
# confluence_get_space_property_by_id

`GET /spaces/{space-id}/properties/{property-id}` — Get space property by id

- Request: [[Confluence v2 - Get space property by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
