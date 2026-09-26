---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-properties
  - api/operation/get
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_content_property_for_custom_content_by_id
title: "Confluence v2 - Get content property for custom content by id"
kind: request
request: "[[Confluence v2 - Get content property for custom content by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /custom-content/{custom-content-id}/properties/{property-id} · Get content property for custom content by id. Retrieves a specific Content Property by ID that is attached to a specified custom content. Permissions required: Permission to view the page. Writes data: no."
params:
  "custom_content_id":
    type: string
    required: true
    description: "The ID of the custom content for which content properties should be returned."
  "property_id":
    type: string
    required: true
    description: "The ID of the content property being requested."
writes: false
expose: false
---
# confluence_get_content_property_for_custom_content_by_id

`GET /custom-content/{custom-content-id}/properties/{property-id}` — Get content property for custom content by id

- Request: [[Confluence v2 - Get content property for custom content by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
