---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttype
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_post_objecttype_position
title: "Assets - POST objecttype {id} position"
kind: request
request: "[[Assets - POST objecttype {id} position]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /objecttype/{id}/position · /objecttype/{id}/position. Change position of this object type Writes data: yes."
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
# assets_post_objecttype_position

`POST /objecttype/{id}/position` — /objecttype/{id}/position

- Request: [[Assets - POST objecttype {id} position]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
