---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/config
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_post_config_referencetype
title: "Assets - POST config referencetype"
kind: request
request: "[[Assets - POST config referencetype]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /config/referencetype · /config/referencetype. Update a reference type Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# assets_post_config_referencetype

`POST /config/referencetype` — /config/referencetype

- Request: [[Assets - POST config referencetype]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
