---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_update_object
title: "Assets - PUT object {id}"
kind: request
request: "[[Assets - PUT object {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · PUT /object/{id} · /object/{id}. Update an existing object in Assets Writes data: yes."
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
# assets_update_object

`PUT /object/{id}` — /object/{id}

- Request: [[Assets - PUT object {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
