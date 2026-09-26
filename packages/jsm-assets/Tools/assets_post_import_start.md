---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/import
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_post_import_start
title: "Assets - POST import start {id}"
kind: request
request: "[[Assets - POST import start {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /import/start/{id} · /import/start/{id}. Start configured imports. To see an ongoing import see the Progress resource Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: true
expose: false
---
# assets_post_import_start

`POST /import/start/{id}` — /import/start/{id}

- Request: [[Assets - POST import start {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
