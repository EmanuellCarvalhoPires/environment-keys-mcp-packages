---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_spaces
title: "Confluence v2 - Get spaces"
kind: request
request: "[[Confluence v2 - Get spaces]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /spaces · Get spaces. Returns all spaces. The results will be sorted by id ascending. The number of results is limited by the limit parameter and additional results (if available) will be available through the next URL present in the Link response header. Writes data: no."
params:
  "ids":
    type: string
    required: false
    description: "Filter the results to spaces based on their IDs. Multiple IDs can be specified as a comma-separated list."
  "keys":
    type: string
    required: false
    description: "Filter the results to spaces based on their keys. Multiple keys can be specified as a comma-separated list."
  "type":
    type: string
    required: false
    description: "Filter the results to spaces based on their type."
  "status":
    type: string
    required: false
    description: "Filter the results to spaces based on their status."
  "labels":
    type: string
    required: false
    description: "Filter the results to spaces based on their labels. Multiple labels can be specified as a comma-separated list."
  "favorited_by":
    type: string
    required: false
    description: "Filter the results to spaces favorited by the user with the specified account ID."
  "not_favorited_by":
    type: string
    required: false
    description: "Filter the results to spaces NOT favorited by the user with the specified account ID."
  "sort":
    type: string
    required: false
    description: "Used to sort the result by a particular field."
  "description_format":
    type: string
    required: false
    description: "The content format type to be returned in the description field of the response. If available, the representation will be available under a response field of the same name under the description field."
  "include_icon":
    type: string
    required: false
    description: "If the icon for the space should be fetched or not."
  "cursor":
    type: string
    required: false
    description: "Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results."
  "limit":
    type: string
    required: false
    description: "Maximum number of spaces per result to return. If more results exist, use the Link response header to retrieve a relative URL that will return the next set of results."
writes: false
expose: true
---
# confluence_get_spaces

`GET /spaces` — Get spaces

- Request: [[Confluence v2 - Get spaces]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
