---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/space-properties
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_space_properties_in_space
title: "Confluence v2 - Get space properties in space"
kind: request
request: "[[Confluence v2 - Get space properties in space]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /spaces/{space-id}/properties · Get space properties in space. Returns all properties for the given space. Space properties are a key-value storage associated with a space. The limit parameter specifies the maximum number of results returned in a single response. Use the link response header to paginate through additional results. Writes data: no."
params:
  "space_id":
    type: string
    required: true
    description: "The ID of the space for which space properties should be returned."
  "key":
    type: string
    required: false
    description: "The key of the space property to retrieve. This should be used when a user knows the key of their property, but needs to retrieve the id for use in other methods."
  "cursor":
    type: string
    required: false
    description: "Used for pagination, this opaque cursor will be returned in the next URL in the Link response header. Use the relative URL in the Link header to retrieve the next set of results."
  "limit":
    type: string
    required: false
    description: "Maximum number of pages per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results."
writes: false
expose: false
---
# confluence_get_space_properties_in_space

`GET /spaces/{space-id}/properties` — Get space properties in space

- Request: [[Confluence v2 - Get space properties in space]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
