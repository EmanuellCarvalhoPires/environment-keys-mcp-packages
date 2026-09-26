---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttypeattribute
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_delete_objecttypeattribute
title: "Assets - DELETE objecttypeattribute {id}"
kind: request
request: "[[Assets - DELETE objecttypeattribute {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · DELETE /objecttypeattribute/{id} · /objecttypeattribute/{id}. Delete an existing object type attribute Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: true
expose: false
---
# assets_delete_objecttypeattribute

`DELETE /objecttypeattribute/{id}` — /objecttypeattribute/{id}

- Request: [[Assets - DELETE objecttypeattribute {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
