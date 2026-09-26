---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/operation
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_permitted_operations_for_blog_post
title: "Confluence v2 - Get permitted operations for blog post"
kind: request
request: "[[Confluence v2 - Get permitted operations for blog post]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /blogposts/{id}/operations · Get permitted operations for blog post. Returns the permitted operations on specific blog post. Permissions required: Permission to view the parent content of the blog post and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the blog post for which operations should be returned."
writes: false
expose: false
---
# confluence_get_permitted_operations_for_blog_post

`GET /blogposts/{id}/operations` — Get permitted operations for blog post

- Request: [[Confluence v2 - Get permitted operations for blog post]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
