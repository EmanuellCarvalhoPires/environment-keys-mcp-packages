---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttype
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_delete_objecttype
title: "Assets - DELETE objecttype {id}"
kind: request
request: "[[Assets - DELETE objecttype {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · DELETE /objecttype/{id} · /objecttype/{id}. Delete an object type Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: true
expose: false
---
# assets_delete_objecttype

`DELETE /objecttype/{id}` — /objecttype/{id}

- Request: [[Assets - DELETE objecttype {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
