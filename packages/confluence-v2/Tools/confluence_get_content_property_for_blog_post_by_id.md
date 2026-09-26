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
tool: confluence_get_content_property_for_blog_post_by_id
title: "Confluence v2 - Get content property for blog post by id"
kind: request
request: "[[Confluence v2 - Get content property for blog post by id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /blogposts/{blogpost-id}/properties/{property-id} · Get content property for blog post by id. Retrieves a specific Content Property by ID that is attached to a specified blog post. Permissions required: Permission to view the blog post. Writes data: no."
params:
  "blogpost_id":
    type: string
    required: true
    description: "The ID of the blog post for which content properties should be returned."
  "property_id":
    type: string
    required: true
    description: "The ID of the property being requested"
writes: false
expose: false
---
# confluence_get_content_property_for_blog_post_by_id

`GET /blogposts/{blogpost-id}/properties/{property-id}` — Get content property for blog post by id

- Request: [[Confluence v2 - Get content property for blog post by id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
