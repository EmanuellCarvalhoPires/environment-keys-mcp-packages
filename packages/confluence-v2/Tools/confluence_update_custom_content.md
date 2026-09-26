---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/custom-content
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_update_custom_content
title: "Confluence v2 - Update custom content"
kind: request
request: "[[Confluence v2 - Update custom content]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · PUT /custom-content/{id} · Update custom content. Update a custom content by id. At most one of spaceId, pageId, blogPostId, or customContentId is allowed in the request body. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the custom content to be updated. If you don't know the custom content ID, use Get Custom Content by Type and filter the results."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_update_custom_content

`PUT /custom-content/{id}` — Update custom content

- Request: [[Confluence v2 - Update custom content]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
