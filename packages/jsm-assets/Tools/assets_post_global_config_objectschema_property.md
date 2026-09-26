---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/global
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_post_global_config_objectschema_property
title: "Assets - POST global config objectschema {id} property"
kind: request
request: "[[Assets - POST global config objectschema {id} property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /global/config/objectschema/{id}/property · /global/config/objectschema/{id}/property. Update general configuration for object schema Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Object schema id"
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# assets_post_global_config_objectschema_property

`POST /global/config/objectschema/{id}/property` — /global/config/objectschema/{id}/property

- Request: [[Assets - POST global config objectschema {id} property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
