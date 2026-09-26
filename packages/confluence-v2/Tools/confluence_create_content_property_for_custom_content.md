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
tool: confluence_create_content_property_for_custom_content
title: "Confluence v2 - Create content property for custom content"
kind: request
request: "[[Confluence v2 - Create content property for custom content]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /custom-content/{custom-content-id}/properties · Create content property for custom content. Creates a new content property for a piece of custom content. Permissions required: Permission to update the custom content. Writes data: yes."
params:
  "custom_content_id":
    type: string
    required: true
    description: "The ID of the custom content to create a property for."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_content_property_for_custom_content

`POST /custom-content/{custom-content-id}/properties` — Create content property for custom content

- Request: [[Confluence v2 - Create content property for custom content]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
