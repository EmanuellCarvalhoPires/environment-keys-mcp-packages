---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objectschema
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_delete_objectschema
title: "Assets - DELETE objectschema {id}"
kind: request
request: "[[Assets - DELETE objectschema {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · DELETE /objectschema/{id} · /objectschema/{id}. Delete a schema Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: true
expose: false
---
# assets_delete_objectschema

`DELETE /objectschema/{id}` — /objectschema/{id}

- Request: [[Assets - DELETE objectschema {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
