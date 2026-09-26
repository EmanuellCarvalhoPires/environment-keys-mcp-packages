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
tool: confluence_create_content_property_for_smart_link_in_the_content
title: "Confluence v2 - Create content property for Smart Link in the content tree"
kind: request
request: "[[Confluence v2 - Create content property for Smart Link in the content tree]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /embeds/{id}/properties · Create content property for Smart Link in the content tree. Creates a new content property for a Smart Link in the content tree. Permissions required: Permission to update the Smart Link in the content tree. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the Smart Link in the content tree to create a property for."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_content_property_for_smart_link_in_the_content

`POST /embeds/{id}/properties` — Create content property for Smart Link in the content tree

- Request: [[Confluence v2 - Create content property for Smart Link in the content tree]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
