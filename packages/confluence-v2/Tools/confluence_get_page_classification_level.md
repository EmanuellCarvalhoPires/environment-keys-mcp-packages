---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/confluence
  - api/resource/classification-level
  - api/operation/list
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
tool: confluence_get_page_classification_level
title: "Confluence v2 - Get page classification level"
kind: request
request: "[[Confluence v2 - Get page classification level]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /pages/{id}/classification-level · Get page classification level. Returns the classification level for a specific page. Permissions required: 'Permission to access the Confluence site ('Can use' global permission) and permission to view the page. 'Permission to edit the page is required if trying to view classification level for a draft. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the page for which classification level should be returned."
  "status":
    type: string
    required: false
    description: "Status of page from which classification level will fetched."
writes: false
expose: false
---
# confluence_get_page_classification_level

`GET /pages/{id}/classification-level` — Get page classification level

- Request: [[Confluence v2 - Get page classification level]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
