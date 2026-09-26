---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttype
  - api/operation/create
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_post_objecttype_create
title: "Assets - POST objecttype create"
kind: request
request: "[[Assets - POST objecttype create]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /objecttype/create · /objecttype/create. Create a new object type Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# assets_post_objecttype_create

`POST /objecttype/create` — /objecttype/create

- Request: [[Assets - POST objecttype create]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
