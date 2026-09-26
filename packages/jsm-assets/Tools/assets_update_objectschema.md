---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectschema
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_update_objectschema
title: "Assets - PUT objectschema {id}"
kind: request
request: "[[Assets - PUT objectschema {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · PUT /objectschema/{id} · /objectschema/{id}. Update an object schema Writes data: yes."
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
# assets_update_objectschema

`PUT /objectschema/{id}` — /objectschema/{id}

- Request: [[Assets - PUT objectschema {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
