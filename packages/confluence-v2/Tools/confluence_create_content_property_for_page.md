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
tool: confluence_create_content_property_for_page
title: "Confluence v2 - Create content property for page"
kind: request
request: "[[Confluence v2 - Create content property for page]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /pages/{page-id}/properties · Create content property for page. Creates a new content property for a page. Permissions required: Permission to update the page. Writes data: yes."
params:
  "page_id":
    type: string
    required: true
    description: "The ID of the page to create a property for."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_content_property_for_page

`POST /pages/{page-id}/properties` — Create content property for page

- Request: [[Confluence v2 - Create content property for page]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
