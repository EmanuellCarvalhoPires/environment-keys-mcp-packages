---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttypeattribute
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_post_objecttypeattribute
title: "Assets - POST objecttypeattribute {objectTypeId}"
kind: request
request: "[[Assets - POST objecttypeattribute {objectTypeId}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /objecttypeattribute/{objectTypeId} · /objecttypeattribute/{objectTypeId}. Create a new attribute on the given object type Writes data: yes."
params:
  "objectTypeId":
    type: string
    required: true
    description: "Value of objectTypeId in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# assets_post_objecttypeattribute

`POST /objecttypeattribute/{objectTypeId}` — /objecttypeattribute/{objectTypeId}

- Request: [[Assets - POST objecttypeattribute {objectTypeId}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
