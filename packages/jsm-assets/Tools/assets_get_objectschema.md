---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectschema
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_objectschema
title: "Assets - GET objectschema {id}"
kind: request
request: "[[Assets - GET objectschema {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /objectschema/{id} · /objectschema/{id}. Find a schema by id Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: false
expose: false
---
# assets_get_objectschema

`GET /objectschema/{id}` — /objectschema/{id}

- Request: [[Assets - GET objectschema {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
