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
tool: confluence_update_page
title: "Confluence v2 - Update page"
kind: request
request: "[[Confluence v2 - Update page]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · PUT /pages/{id} · Update page. Update a page by id. When the \"current\" version is updated, the provided body content is considered as the latest version. This latest body content will be attempted to be merged into the draft version through a content reconciliation algorithm. Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "The ID of the page to be updated. If you don't know the page ID, use Get Pages and filter the results."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: true
---
# confluence_update_page

`PUT /pages/{id}` — Update page

- Request: [[Confluence v2 - Update page]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
