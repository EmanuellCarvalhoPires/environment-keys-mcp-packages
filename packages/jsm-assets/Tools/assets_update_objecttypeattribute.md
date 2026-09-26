---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttypeattribute
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_update_objecttypeattribute
title: "Assets - PUT objecttypeattribute {objectTypeId} {id}"
kind: request
request: "[[Assets - PUT objecttypeattribute {objectTypeId} {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · PUT /objecttypeattribute/{objectTypeId}/{id} · /objecttypeattribute/{objectTypeId}/{id}. Update an existing object type attribute Writes data: yes."
params:
  "objectTypeId":
    type: string
    required: true
    description: "Value of objectTypeId in the path."
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
# assets_update_objecttypeattribute

`PUT /objecttypeattribute/{objectTypeId}/{id}` — /objecttypeattribute/{objectTypeId}/{id}

- Request: [[Assets - PUT objecttypeattribute {objectTypeId} {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
