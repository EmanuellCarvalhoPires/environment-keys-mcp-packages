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
tool: confluence_get_account_ids_of_likes_for_inline_comment
title: "Confluence v2 - Get account IDs of likes for inline comment"
kind: request
request: "[[Confluence v2 - Get account IDs of likes for inline comment]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /inline-comments/{id}/likes/users · Get account IDs of likes for inline comment. Returns the account IDs of likes of specific inline comment. Permissions required: Permission to view the content of the page/blogpost and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the inline comment for which like count should be returned."
  "cursor":
    type: string
    required: false
    description: "Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results."
  "limit":
    type: string
    required: false
    description: "Maximum number of account IDs per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results."
writes: false
expose: false
---
# confluence_get_account_ids_of_likes_for_inline_comment

`GET /inline-comments/{id}/likes/users` — Get account IDs of likes for inline comment

- Request: [[Confluence v2 - Get account IDs of likes for inline comment]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
