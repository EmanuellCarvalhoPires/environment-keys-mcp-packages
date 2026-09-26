---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/config
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_post_config_statustype
title: "Assets - POST config statustype"
kind: request
request: "[[Assets - POST config statustype]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /config/statustype · /config/statustype. Create a new status Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# assets_post_config_statustype

`POST /config/statustype` — /config/statustype

- Request: [[Assets - POST config statustype]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
