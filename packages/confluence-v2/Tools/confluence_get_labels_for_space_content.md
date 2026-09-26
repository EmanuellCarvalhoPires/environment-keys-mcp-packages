---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/label
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_labels_for_space_content
title: "Confluence v2 - Get labels for space content"
kind: request
request: "[[Confluence v2 - Get labels for space content]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /spaces/{id}/content/labels · Get labels for space content. Returns the labels of space content (pages, blogposts etc). The number of results is limited by the limit parameter and additional results (if available) will be available through the next URL present in the Link response header. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the space for which labels should be returned."
  "prefix":
    type: string
    required: false
    description: "Filter the results to labels based on their prefix."
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
    description: "Maximum number of labels per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results."
writes: false
expose: false
---
# confluence_get_labels_for_space_content

`GET /spaces/{id}/content/labels` — Get labels for space content

- Request: [[Confluence v2 - Get labels for space content]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
