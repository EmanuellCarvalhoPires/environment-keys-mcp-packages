---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/objecttype
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_objecttype
title: "Assets - GET objecttype {id}"
kind: request
request: "[[Assets - GET objecttype {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /objecttype/{id} · /objecttype/{id}. Find an object type by id Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: false
expose: false
---
# assets_get_objecttype

`GET /objecttype/{id}` — /objecttype/{id}

- Request: [[Assets - GET objecttype {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
