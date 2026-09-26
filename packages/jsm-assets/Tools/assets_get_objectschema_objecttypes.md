---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectschema
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_objectschema_objecttypes
title: "Assets - GET objectschema {id} objecttypes"
kind: request
request: "[[Assets - GET objectschema {id} objecttypes]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /objectschema/{id}/objecttypes · /objectschema/{id}/objecttypes. Find all object types for this object schema Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: false
expose: false
---
# assets_get_objectschema_objecttypes

`GET /objectschema/{id}/objecttypes` — /objectschema/{id}/objecttypes

- Request: [[Assets - GET objectschema {id} objecttypes]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
