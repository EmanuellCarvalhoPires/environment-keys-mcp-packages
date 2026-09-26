---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-properties
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_create_content_property_for_whiteboard
title: "Confluence v2 - Create content property for whiteboard"
kind: request
request: "[[Confluence v2 - Create content property for whiteboard]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /whiteboards/{id}/properties · Create content property for whiteboard. Creates a new content property for a whiteboard. Permissions required: Permission to update the whiteboard. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the whiteboard to create a property for."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_content_property_for_whiteboard

`POST /whiteboards/{id}/properties` — Create content property for whiteboard

- Request: [[Confluence v2 - Create content property for whiteboard]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
