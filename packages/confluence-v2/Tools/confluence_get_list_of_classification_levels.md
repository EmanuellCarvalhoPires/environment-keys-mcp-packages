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
tool: confluence_get_list_of_classification_levels
title: "Confluence v2 - Get list of classification levels"
kind: request
request: "[[Confluence v2 - Get list of classification levels]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Confluence v2 · GET /classification-levels · Get list of classification levels. Returns a list of classification levels available. Permissions required: 'Permission to access the Confluence site ('Can use' global permission). Writes data: no."
writes: false
expose: false
---
# confluence_get_list_of_classification_levels

`GET /classification-levels` — Get list of classification levels

- Request: [[Confluence v2 - Get list of classification levels]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
