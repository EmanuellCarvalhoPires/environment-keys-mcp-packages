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
tool: confluence_v1_copy_page_hierarchy
title: "Confluence v1 - Copy page hierarchy"
kind: request
request: "[[Confluence v1 - Copy page hierarchy]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v1 · POST /wiki/rest/api/content/{id}/pagehierarchy/copy · Copy page hierarchy. Copy page hierarchy allows the copying of an entire hierarchy of pages and their associated properties, permissions and attachments. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# confluence_v1_copy_page_hierarchy

`POST /wiki/rest/api/content/{id}/pagehierarchy/copy` — Copy page hierarchy

- Request: [[Confluence v1 - Copy page hierarchy]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
