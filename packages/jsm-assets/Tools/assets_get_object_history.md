---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_object_history
title: "Assets - GET object {id} history"
kind: request
request: "[[Assets - GET object {id} history]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /object/{id}/history · /object/{id}/history. Retrieve the history entries for this object Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
  "asc":
    type: string
    required: false
    description: "Should the history be retrieved in ascending order"
writes: false
expose: false
---
# assets_get_object_history

`GET /object/{id}/history` — /object/{id}/history

- Request: [[Assets - GET object {id} history]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
