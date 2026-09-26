---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/blog-post
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_create_blog_post
title: "Confluence v2 - Create blog post"
kind: request
request: "[[Confluence v2 - Create blog post]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · POST /blogposts · Create blog post. Creates a new blog post in the space specified by the spaceId. By default this will create the blog post as a non-draft, unless the status is specified as draft. If creating a non-draft, the title must not be empty. Writes data: yes."
params:
  "private":
    type: string
    required: false
    description: "The blog post will be private. Only the user who creates this blog post will have permission to view and edit one."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_create_blog_post

`POST /blogposts` — Create blog post

- Request: [[Confluence v2 - Create blog post]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
