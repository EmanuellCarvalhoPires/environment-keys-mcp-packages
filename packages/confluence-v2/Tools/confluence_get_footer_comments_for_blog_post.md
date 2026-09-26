---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/comment
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_footer_comments_for_blog_post
title: "Confluence v2 - Get footer comments for blog post"
kind: request
request: "[[Confluence v2 - Get footer comments for blog post]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /blogposts/{id}/footer-comments · Get footer comments for blog post. Returns the root footer comments of specific blog post. The number of results is limited by the limit parameter and additional results (if available) will be available through the next URL present in the Link response header. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the blog post for which footer comments should be returned."
  "body_format":
    type: string
    required: false
    description: "The content format type to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field."
  "status":
    type: string
    required: false
    description: "Filter the footer comment being retrieved by its status."
  "sort":
    type: string
    required: false
    description: "Used to sort the result by a particular field."
  "cursor":
    type: string
    required: false
    description: "Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results."
  "limit":
    type: string
    required: false
    description: "Maximum number of footer comments per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results."
writes: false
expose: false
---
# confluence_get_footer_comments_for_blog_post

`GET /blogposts/{id}/footer-comments` — Get footer comments for blog post

- Request: [[Confluence v2 - Get footer comments for blog post]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
