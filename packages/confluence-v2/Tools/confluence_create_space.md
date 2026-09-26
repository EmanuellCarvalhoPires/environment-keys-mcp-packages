---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_create_space
title: "Confluence v2 - Create space"
kind: request
request: "[[Confluence v2 - Create space]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /spaces · Create space. Creates a Space as specified in the payload. Available on tenants with Role-Based Access Control. Permissions required: Permission to create spaces. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_space

`POST /spaces` — Create space

- Request: [[Confluence v2 - Create space]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
