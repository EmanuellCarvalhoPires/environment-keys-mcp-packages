---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_delete_object
title: "Assets - DELETE object {id}"
kind: request
request: "[[Assets - DELETE object {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · DELETE /object/{id} · /object/{id}. Delete the referenced object Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: true
expose: false
---
# assets_delete_object

`DELETE /object/{id}` — /object/{id}

- Request: [[Assets - DELETE object {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
