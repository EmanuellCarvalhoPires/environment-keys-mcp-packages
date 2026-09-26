---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/custom-content
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_custom_content_by_type
title: "Confluence v2 - Get custom content by type"
kind: request
request: "[[Confluence v2 - Get custom content by type]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /custom-content · Get custom content by type. Returns all custom content for a given type. The number of results is limited by the limit parameter and additional results (if available) will be available through the next URL present in the Link response header. Writes data: no."
params:
  "type":
    type: string
    required: true
    description: "The type of custom content being requested. See: https://developer.atlassian.com/cloud/confluence/custom-content/ for additional details on custom content."
  "id":
    type: string
    required: false
    description: "Filter the results based on custom content ids. Multiple custom content ids can be specified as a comma-separated list."
  "space_id":
    type: string
    required: false
    description: "Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list."
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
    description: "Maximum number of pages per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results."
  "body_format":
    type: string
    required: false
    description: "The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field."
writes: false
expose: false
---
# confluence_get_custom_content_by_type

`GET /custom-content` — Get custom content by type

- Request: [[Confluence v2 - Get custom content by type]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
