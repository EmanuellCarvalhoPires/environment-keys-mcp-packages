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
tool: confluence_get_like_count_for_inline_comment
title: "Confluence v2 - Get like count for inline comment"
kind: request
request: "[[Confluence v2 - Get like count for inline comment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /inline-comments/{id}/likes/count · Get like count for inline comment. Returns the count of likes of specific inline comment. Permissions required: Permission to view the content of the page/blogpost and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the inline comment for which like count should be returned."
writes: false
expose: false
---
# confluence_get_like_count_for_inline_comment

`GET /inline-comments/{id}/likes/count` — Get like count for inline comment

- Request: [[Confluence v2 - Get like count for inline comment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
