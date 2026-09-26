---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttype
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_update_objecttype
title: "Assets - PUT objecttype {id}"
kind: request
request: "[[Assets - PUT objecttype {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · PUT /objecttype/{id} · /objecttype/{id}. Update an existing object type Writes data: yes."
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
# assets_update_objecttype

`PUT /objecttype/{id}` — /objecttype/{id}

- Request: [[Assets - PUT objecttype {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
