---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/config
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_config_referencetype
title: "Assets - GET config referencetype"
kind: request
request: "[[Assets - GET config referencetype]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /config/referencetype · /config/referencetype. Get reference type Writes data: no."
params:
  "objectSchemaId":
    type: string
    required: false
    description: "Include reference types for the object schema id. If supplied reference types for the object schema will be returned otherwise all global will be returned"
  "includeAll":
    type: string
    required: false
    description: "Include all reference types. Defaults to false"
writes: false
expose: false
---
# assets_get_config_referencetype

`GET /config/referencetype` — /config/referencetype

- Request: [[Assets - GET config referencetype]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
