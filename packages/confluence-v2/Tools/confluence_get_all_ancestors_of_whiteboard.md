---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/ancestors
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_all_ancestors_of_whiteboard
title: "Confluence v2 - Get all ancestors of whiteboard"
kind: request
request: "[[Confluence v2 - Get all ancestors of whiteboard]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /whiteboards/{id}/ancestors · Get all ancestors of whiteboard. Returns all ancestors for a given whiteboard by ID in top-to-bottom order (that is, the highest ancestor is the first item in the response payload). Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the whiteboard."
  "limit":
    type: string
    required: false
    description: "Maximum number of items per result to return. If more results exist, call the endpoint with the highest ancestor's ID to fetch the next set of results."
writes: false
expose: false
---
# confluence_get_all_ancestors_of_whiteboard

`GET /whiteboards/{id}/ancestors` — Get all ancestors of whiteboard

- Request: [[Confluence v2 - Get all ancestors of whiteboard]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
