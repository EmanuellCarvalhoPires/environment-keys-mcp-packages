---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/data-policies
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_spaces_with_data_policies
title: "Confluence v2 - Get spaces with data policies"
kind: request
request: "[[Confluence v2 - Get spaces with data policies]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /data-policies/spaces · Get spaces with data policies. Returns all spaces. The results will be sorted by id ascending. The number of results is limited by the limit parameter and additional results (if available) will be available through the next URL present in the Link response header. Writes data: no."
params:
  "ids":
    type: string
    required: false
    description: "Filter the results to spaces based on their IDs. Multiple IDs can be specified as a comma-separated list."
  "keys":
    type: string
    required: false
    description: "Filter the results to spaces based on their keys. Multiple keys can be specified as a comma-separated list."
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
    description: "Maximum number of spaces per result to return. If more results exist, use the Link response header to retrieve a relative URL that will return the next set of results."
writes: false
expose: false
---
# confluence_get_spaces_with_data_policies

`GET /data-policies/spaces` — Get spaces with data policies

- Request: [[Confluence v2 - Get spaces with data policies]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
