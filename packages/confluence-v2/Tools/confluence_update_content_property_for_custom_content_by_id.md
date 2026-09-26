---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-properties
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_update_content_property_for_custom_content_by_id
title: "Confluence v2 - Update content property for custom content by id"
kind: request
request: "[[Confluence v2 - Update content property for custom content by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · PUT /custom-content/{custom-content-id}/properties/{property-id} · Update content property for custom content by id. Update a content property for a piece of custom content by its id. Permissions required: Permission to edit the custom content. Writes data: yes."
params:
  "custom_content_id":
    type: string
    required: true
    description: "The ID of the custom content the property belongs to."
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
# confluence_update_content_property_for_custom_content_by_id

`PUT /custom-content/{custom-content-id}/properties/{property-id}` — Update content property for custom content by id

- Request: [[Confluence v2 - Update content property for custom content by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
