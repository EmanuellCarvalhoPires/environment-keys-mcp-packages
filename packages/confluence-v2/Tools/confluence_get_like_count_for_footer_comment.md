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
tool: confluence_get_like_count_for_footer_comment
title: "Confluence v2 - Get like count for footer comment"
kind: request
request: "[[Confluence v2 - Get like count for footer comment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /footer-comments/{id}/likes/count · Get like count for footer comment. Returns the count of likes of specific footer comment. Permissions required: Permission to view the content of the page/blogpost and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the footer comment for which like count should be returned."
writes: false
expose: false
---
# confluence_get_like_count_for_footer_comment

`GET /footer-comments/{id}/likes/count` — Get like count for footer comment

- Request: [[Confluence v2 - Get like count for footer comment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
