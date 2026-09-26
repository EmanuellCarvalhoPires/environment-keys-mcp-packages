---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/update
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_update_restrictions
title: "Confluence v1 - Update restrictions"
kind: request
request: "[[Confluence v1 - Update restrictions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · PUT /wiki/rest/api/content/{id}/restriction · Update restrictions. Updates restrictions for a piece of content. This removes the existing restrictions and replaces them with the restrictions in the request. Permissions required: Permission to edit the content. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content to update restrictions for."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the content restrictions (returned in response) to expand."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_update_restrictions

`PUT /wiki/rest/api/content/{id}/restriction` — Update restrictions

- Request: [[Confluence v1 - Update restrictions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
