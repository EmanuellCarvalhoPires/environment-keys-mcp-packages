---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/progress
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_progress_category_imports
title: "Assets - GET progress category imports {id}"
kind: request
request: "[[Assets - GET progress category imports {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /progress/category/imports/{id} · /progress/category/imports/{id}. Show ongoing import process Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: false
expose: false
---
# assets_get_progress_category_imports

`GET /progress/category/imports/{id}` — /progress/category/imports/{id}

- Request: [[Assets - GET progress category imports {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
