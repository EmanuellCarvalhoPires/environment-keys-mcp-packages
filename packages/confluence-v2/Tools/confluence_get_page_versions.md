---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/version
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_page_versions
title: "Confluence v2 - Get page versions"
kind: request
request: "[[Confluence v2 - Get page versions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /pages/{id}/versions · Get page versions. Returns the versions of specific page. Permissions required: Permission to view the page and its corresponding space. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the page to be queried for its versions. If you don't know the page ID, use Get pages and filter the results."
  "body_format":
    type: string
    required: false
    description: "The content format types to be returned in the body field of the response. If available, the representation will be available under a response field of the same name under the body field."
  "cursor":
    type: string
    required: false
    description: "Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results."
  "limit":
    type: string
    required: false
    description: "Maximum number of versions per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results."
  "sort":
    type: string
    required: false
    description: "Used to sort the result by a particular field."
writes: false
expose: false
---
# confluence_get_page_versions

`GET /pages/{id}/versions` — Get page versions

- Request: [[Confluence v2 - Get page versions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
