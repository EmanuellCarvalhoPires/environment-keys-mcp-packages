---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_object
title: "Assets - GET object {id}"
kind: request
request: "[[Assets - GET object {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /object/{id} · /object/{id}. Load one object Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: false
expose: true
---
# assets_get_object

`GET /object/{id}` — /object/{id}

- Request: [[Assets - GET object {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
