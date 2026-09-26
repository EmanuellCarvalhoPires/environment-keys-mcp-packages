---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectschema
  - api/operation/create
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_post_objectschema_create
title: "Assets - POST objectschema create"
kind: request
request: "[[Assets - POST objectschema create]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /objectschema/create · /objectschema/create. Create a new object schema Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# assets_post_objectschema_create

`POST /objectschema/create` — /objectschema/create

- Request: [[Assets - POST objectschema create]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
