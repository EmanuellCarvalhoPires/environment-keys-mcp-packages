---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/icon
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_icon
title: "Assets - GET icon {id}"
kind: request
request: "[[Assets - GET icon {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /icon/{id} · /icon/{id}. Load a single icon by id Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: false
expose: false
---
# assets_get_icon

`GET /icon/{id}` — /icon/{id}

- Request: [[Assets - GET icon {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
