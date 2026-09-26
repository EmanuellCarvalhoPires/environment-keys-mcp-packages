---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/custom-content
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_create_custom_content
title: "Confluence v2 - Create custom content"
kind: request
request: "[[Confluence v2 - Create custom content]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /custom-content · Create custom content. Creates a new custom content in the given space, page, blogpost or other custom content. Only one of spaceId, pageId, blogPostId, or customContentId is required in the request body. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_custom_content

`POST /custom-content` — Create custom content

- Request: [[Confluence v2 - Create custom content]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
