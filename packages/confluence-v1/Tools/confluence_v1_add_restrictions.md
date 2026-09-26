---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-restrictions
  - api/operation/create
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_add_restrictions
title: "Confluence v1 - Add restrictions"
kind: request
request: "[[Confluence v1 - Add restrictions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/content/{id}/restriction · Add restrictions. Adds restrictions to a piece of content. Note, this does not change any existing restrictions on the content. Permissions required: Permission to edit the content. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the content to add restrictions to."
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
# confluence_v1_add_restrictions

`POST /wiki/rest/api/content/{id}/restriction` — Add restrictions

- Request: [[Confluence v1 - Add restrictions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
