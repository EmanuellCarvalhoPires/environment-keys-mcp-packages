---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/blog-post
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_update_blog_post
title: "Confluence v2 - Update blog post"
kind: request
request: "[[Confluence v2 - Update blog post]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · PUT /blogposts/{id} · Update blog post. Update a blog post by id. Permissions required: Permission to view the blog post and its corresponding space. Permission to update blog posts in the space. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the blog post to be updated. If you don't know the blog post ID, use Get Blog Posts and filter the results."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_update_blog_post

`PUT /blogposts/{id}` — Update blog post

- Request: [[Confluence v2 - Update blog post]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
