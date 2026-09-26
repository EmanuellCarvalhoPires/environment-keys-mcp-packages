---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/whiteboard
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_create_whiteboard
title: "Confluence v2 - Create whiteboard"
kind: request
request: "[[Confluence v2 - Create whiteboard]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /whiteboards · Create whiteboard. Creates a whiteboard in the space. Permissions required: Permission to view the corresponding space. Permission to create a whiteboard in the space. Writes data: yes."
params:
  "private":
    type: string
    required: false
    description: "The whiteboard will be private. Only the user who creates this whiteboard will have permission to view and edit one."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_whiteboard

`POST /whiteboards` — Create whiteboard

- Request: [[Confluence v2 - Create whiteboard]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
