---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/object
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_object_referenceinfo
title: "Assets - GET object {id} referenceinfo"
kind: request
request: "[[Assets - GET object {id} referenceinfo]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /object/{id}/referenceinfo · /object/{id}/referenceinfo. Find all references for an object Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: false
expose: false
---
# assets_get_object_referenceinfo

`GET /object/{id}/referenceinfo` — /object/{id}/referenceinfo

- Request: [[Assets - GET object {id} referenceinfo]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
