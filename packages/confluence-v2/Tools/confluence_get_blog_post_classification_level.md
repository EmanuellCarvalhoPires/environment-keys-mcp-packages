---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/classification-level
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_blog_post_classification_level
title: "Confluence v2 - Get blog post classification level"
kind: request
request: "[[Confluence v2 - Get blog post classification level]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /blogposts/{id}/classification-level · Get blog post classification level. Returns the classification level for a specific blog post. Permissions required: 'Permission to access the Confluence site ('Can use' global permission) and permission to view the blog post. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the blog post for which classification level should be returned."
  "status":
    type: string
    required: false
    description: "Status of blog post from which classification level will fetched."
writes: false
expose: false
---
# confluence_get_blog_post_classification_level

`GET /blogposts/{id}/classification-level` — Get blog post classification level

- Request: [[Confluence v2 - Get blog post classification level]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
