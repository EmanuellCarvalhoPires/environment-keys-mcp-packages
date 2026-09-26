---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/create
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_post_object_create
title: "Assets - POST object create"
kind: request
request: "[[Assets - POST object create]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /object/create · /object/create. Create a new object in Assets Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: true
---
# assets_post_object_create

`POST /object/create` — /object/create

- Request: [[Assets - POST object create]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
