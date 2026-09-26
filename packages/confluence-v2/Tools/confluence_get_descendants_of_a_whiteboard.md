---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/descendants
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_descendants_of_a_whiteboard
title: "Confluence v2 - Get descendants of a whiteboard"
kind: request
request: "[[Confluence v2 - Get descendants of a whiteboard]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /whiteboards/{id}/descendants · Get descendants of a whiteboard. Returns descendants in the content tree for a given whiteboard by ID in top-to-bottom order (that is, the highest descendant is the first item in the response payload). Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the whiteboard."
  "limit":
    type: string
    required: false
    description: "Maximum number of items per result to return. If more results exist, call the endpoint with the cursor to fetch the next set of results."
  "depth":
    type: string
    required: false
    description: "Maximum depth of descendants to return. If more results are required, use the endpoint corresponding to the content type of the deepest descendant to fetch more descendants."
  "cursor":
    type: string
    required: false
    description: "Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results."
writes: false
expose: false
---
# confluence_get_descendants_of_a_whiteboard

`GET /whiteboards/{id}/descendants` — Get descendants of a whiteboard

- Request: [[Confluence v2 - Get descendants of a whiteboard]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
