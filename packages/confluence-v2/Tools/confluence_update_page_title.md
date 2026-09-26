---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/page
  - api/operation/update
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_update_page_title
title: "Confluence v2 - Update page title"
kind: request
request: "[[Confluence v2 - Update page title]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · PUT /pages/{id}/title · Update page title. Updates the title of a specified page. Permissions required: Permission to view the page and its corresponding space. Permission to update pages in the space. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the page to be updated. If you don't know the page ID, use Get Pages and filter the results"
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_update_page_title

`PUT /pages/{id}/title` — Update page title

- Request: [[Confluence v2 - Update page title]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
