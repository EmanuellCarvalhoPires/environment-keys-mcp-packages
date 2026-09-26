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
tool: confluence_get_account_ids_of_likes_for_page
title: "Confluence v2 - Get account IDs of likes for page"
kind: request
request: "[[Confluence v2 - Get account IDs of likes for page]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /pages/{id}/likes/users · Get account IDs of likes for page. Returns the account IDs of likes of specific page. Permissions required: Permission to view the content of the page and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the page for which like count should be returned."
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
# confluence_get_account_ids_of_likes_for_page

`GET /pages/{id}/likes/users` — Get account IDs of likes for page

- Request: [[Confluence v2 - Get account IDs of likes for page]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
