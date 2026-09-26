---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-children-and-descendants
  - api/operation/action
  - api/effect/write
  - api/version/v1
up: "[[MCP - Confluence v1]]"
tool: confluence_v1_copy_single_page
title: "Confluence v1 - Copy single page"
kind: request
request: "[[Confluence v1 - Copy single page]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/content/{id}/copy · Copy single page. Copies a single page and its associated properties, permissions, attachments, and custom contents. The id path parameter refers to the content ID of the page to copy. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
  "expand":
    type: string
    required: false
    description: "A multi-value parameter indicating which properties of the content to expand. Maximum sub-expansions allowed is 8."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_copy_single_page

`POST /wiki/rest/api/content/{id}/copy` — Copy single page

- Request: [[Confluence v1 - Copy single page]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
