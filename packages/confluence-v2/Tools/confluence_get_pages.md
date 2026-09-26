---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/page
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_pages
title: "Confluence v2 - Get pages"
kind: request
request: "[[Confluence v2 - Get pages]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /pages · Get pages. Returns all pages. The number of results is limited by the limit parameter and additional results (if available) will be available through the next URL present in the Link response header. Writes data: no."
params:
  "id":
    type: string
    required: false
    description: "Filter the results based on page ids. Multiple page ids can be specified as a comma-separated list."
  "space_id":
    type: string
    required: false
    description: "Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list."
  "sort":
    type: string
    required: false
    description: "Used to sort the result by a particular field."
  "status":
    type: string
    required: false
    description: "Filter the results to pages based on their status. By default, current and archived are used."
  "title":
    type: string
    required: false
    description: "Filter the results to pages based on their title."
  "body_format":
    type: string
    required: false
    description: "The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field."
  "subtype":
    type: string
    required: false
    description: "Filter the results to pages based on their subtype."
  "cursor":
    type: string
    required: false
    description: "Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results."
  "limit":
    type: string
    required: false
    description: "Maximum number of pages per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results."
writes: false
expose: true
---
# confluence_get_pages

`GET /pages` — Get pages

- Request: [[Confluence v2 - Get pages]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
