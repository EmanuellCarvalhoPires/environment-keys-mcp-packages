---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-properties
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_content_properties_for_custom_content
title: "Confluence v2 - Get content properties for custom content"
kind: request
request: "[[Confluence v2 - Get content properties for custom content]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /custom-content/{custom-content-id}/properties · Get content properties for custom content. Retrieves Content Properties tied to a specified custom content. Permissions required: Permission to view the custom content. Writes data: no."
params:
  "custom_content_id":
    type: string
    required: true
    description: "The ID of the custom content for which content properties should be returned."
  "key":
    type: string
    required: false
    description: "Filters the response to return a specific content property with matching key (case sensitive)."
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
    description: "Maximum number of attachments per result to return. If more results exist, use the Link header to retrieve a relative URL that will return the next set of results."
writes: false
expose: false
---
# confluence_get_content_properties_for_custom_content

`GET /custom-content/{custom-content-id}/properties` — Get content properties for custom content

- Request: [[Confluence v2 - Get content properties for custom content]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
