---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/group
  - api/operation/search
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_search_groups_by_partial_query
title: "Confluence v1 - Search groups by partial query"
kind: request
request: "[[Confluence v1 - Search groups by partial query]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · GET /wiki/rest/api/group/picker · Search groups by partial query. Get search results of groups by partial query provided. Writes data: no."
params:
  "query":
    type: string
    required: true
    description: "the search term used to query results."
  "start":
    type: string
    required: false
    description: "The starting index of the returned groups."
  "limit":
    type: string
    required: false
    description: "The maximum number of groups to return per page. Note, this is restricted to a maximum limit of 200 groups."
  "shouldReturnTotalSize":
    type: string
    required: false
    description: "Whether to include total size parameter in the results. Note, fetching total size property is an expensive operation; use it if your use case needs this value."
writes: false
expose: false
---
# confluence_v1_search_groups_by_partial_query

`GET /wiki/rest/api/group/picker` — Search groups by partial query

- Request: [[Confluence v1 - Search groups by partial query]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
