---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_object_attributes
title: "Assets - GET object {id} attributes"
kind: request
request: "[[Assets - GET object {id} attributes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /object/{id}/attributes · /object/{id}/attributes. List all attributes for the given object Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: false
expose: false
---
# assets_get_object_attributes

`GET /object/{id}/attributes` — /object/{id}/attributes

- Request: [[Assets - GET object {id} attributes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
