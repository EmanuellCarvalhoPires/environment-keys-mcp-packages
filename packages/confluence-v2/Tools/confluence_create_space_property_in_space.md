---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-properties
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_create_space_property_in_space
title: "Confluence v2 - Create space property in space"
kind: request
request: "[[Confluence v2 - Create space property in space]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /spaces/{space-id}/properties · Create space property in space. Creates a new space property. Permissions required: Permission to access the Confluence site ('Can use' global permission) and 'Admin' permission for the space. Writes data: yes."
params:
  "space_id":
    type: string
    required: true
    description: "The ID of the space for which space properties should be returned."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_space_property_in_space

`POST /spaces/{space-id}/properties` — Create space property in space

- Request: [[Confluence v2 - Create space property in space]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
