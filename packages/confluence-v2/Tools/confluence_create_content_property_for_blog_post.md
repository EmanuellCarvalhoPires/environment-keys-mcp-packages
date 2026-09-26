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
tool: confluence_create_content_property_for_blog_post
title: "Confluence v2 - Create content property for blog post"
kind: request
request: "[[Confluence v2 - Create content property for blog post]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /blogposts/{blogpost-id}/properties · Create content property for blog post. Creates a new property for a blogpost. Permissions required: Permission to update the blog post. Writes data: yes."
params:
  "blogpost_id":
    type: string
    required: true
    description: "The ID of the blog post to create a property for."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_content_property_for_blog_post

`POST /blogposts/{blogpost-id}/properties` — Create content property for blog post

- Request: [[Confluence v2 - Create content property for blog post]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
