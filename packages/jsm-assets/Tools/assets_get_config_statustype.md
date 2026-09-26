---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/config
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_config_statustype
title: "Assets - GET config statustype"
kind: request
request: "[[Assets - GET config statustype]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /config/statustype · /config/statustype. Find all status Writes data: no."
params:
  "objectSchemaId":
    type: string
    required: false
    description: "Include statuses for the object schema id. If supplied statuses for the object schema will be returned otherwise all global will be returned"
writes: false
expose: false
---
# assets_get_config_statustype

`GET /config/statustype` — /config/statustype

- Request: [[Assets - GET config statustype]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
