---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/children
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_child_custom_content
title: "Confluence v2 - Get child custom content"
kind: request
request: "[[Confluence v2 - Get child custom content]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /custom-content/{id}/children · Get child custom content. Returns all child custom content for given custom content id. The number of results is limited by the limit parameter and additional results (if available) will be available through the next URL present in the Link response header. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the parent custom content. If you don't know the custom content ID, use Get custom-content and filter the results."
  "cursor":
    type: string
    required: false
    description: "Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results."
  "limit":
    type: string
    required: false
    description: "Maximum number of pages per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results."
  "sort":
    type: string
    required: false
    description: "Used to sort the result by a particular field."
writes: false
expose: false
---
# confluence_get_child_custom_content

`GET /custom-content/{id}/children` — Get child custom content

- Request: [[Confluence v2 - Get child custom content]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
