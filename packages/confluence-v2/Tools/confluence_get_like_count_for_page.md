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
tool: confluence_get_like_count_for_page
title: "Confluence v2 - Get like count for page"
kind: request
request: "[[Confluence v2 - Get like count for page]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /pages/{id}/likes/count · Get like count for page. Returns the count of likes of specific page. Permissions required: Permission to view the content of the page and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the page for which like count should be returned."
writes: false
expose: false
---
# confluence_get_like_count_for_page

`GET /pages/{id}/likes/count` — Get like count for page

- Request: [[Confluence v2 - Get like count for page]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
