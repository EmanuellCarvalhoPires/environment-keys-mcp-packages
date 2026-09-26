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
tool: confluence_get_content_property_for_page_by_id
title: "Confluence v2 - Get content property for page by id"
kind: request
request: "[[Confluence v2 - Get content property for page by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /pages/{page-id}/properties/{property-id} · Get content property for page by id. Retrieves a specific Content Property by ID that is attached to a specified page. Permissions required: Permission to view the page. Writes data: no."
params:
  "page_id":
    type: string
    required: true
    description: "The ID of the page for which content properties should be returned."
  "property_id":
    type: string
    required: true
    description: "The ID of the content property being requested."
writes: false
expose: false
---
# confluence_get_content_property_for_page_by_id

`GET /pages/{page-id}/properties/{property-id}` — Get content property for page by id

- Request: [[Confluence v2 - Get content property for page by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
