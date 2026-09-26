---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/like
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_like_count_for_blog_post
title: "Confluence v2 - Get like count for blog post"
kind: request
request: "[[Confluence v2 - Get like count for blog post]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /blogposts/{id}/likes/count · Get like count for blog post. Returns the count of likes of specific blog post. Permissions required: Permission to view the content of the blog post and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the blog post for which like count should be returned."
writes: false
expose: false
---
# confluence_get_like_count_for_blog_post

`GET /blogposts/{id}/likes/count` — Get like count for blog post

- Request: [[Confluence v2 - Get like count for blog post]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
