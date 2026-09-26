---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/blog-post
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_blog_posts_for_label
title: "Confluence v2 - Get blog posts for label"
kind: request
request: "[[Confluence v2 - Get blog posts for label]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /labels/{id}/blogposts · Get blog posts for label. Returns the blogposts of specified label. The number of results is limited by the limit parameter and additional results (if available) will be available through the next URL present in the Link response header. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the label for which blog posts should be returned."
  "space_id":
    type: string
    required: false
    description: "Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list."
  "body_format":
    type: string
    required: false
    description: "The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field."
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
    description: "Maximum number of blog posts per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results."
writes: false
expose: false
---
# confluence_get_blog_posts_for_label

`GET /labels/{id}/blogposts` — Get blog posts for label

- Request: [[Confluence v2 - Get blog posts for label]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
