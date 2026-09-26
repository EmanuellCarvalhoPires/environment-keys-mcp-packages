---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectschema
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_objectschema_objecttypes_flat
title: "Assets - GET objectschema {id} objecttypes flat"
kind: request
request: "[[Assets - GET objectschema {id} objecttypes flat]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /objectschema/{id}/objecttypes/flat · /objectschema/{id}/objecttypes/flat. Find all object types for this object schema Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: false
expose: true
---
# assets_get_objectschema_objecttypes_flat

`GET /objectschema/{id}/objecttypes/flat` — /objectschema/{id}/objecttypes/flat

- Request: [[Assets - GET objectschema {id} objecttypes flat]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
