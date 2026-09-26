---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/classification-level
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_update_blog_post_classification_level
title: "Confluence v2 - Update blog post classification level"
kind: request
request: "[[Confluence v2 - Update blog post classification level]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · PUT /blogposts/{id}/classification-level · Update blog post classification level. Updates the classification level for a specific blog post. Permissions required: 'Permission to access the Confluence site ('Can use' global permission) and permission to edit the blog post. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the blog post for which classification level should be updated."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_update_blog_post_classification_level

`PUT /blogposts/{id}/classification-level` — Update blog post classification level

- Request: [[Confluence v2 - Update blog post classification level]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
