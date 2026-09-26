---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/config
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_config_statustype_get
title: "Assets - GET config statustype {id}"
kind: request
request: "[[Assets - GET config statustype {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /config/statustype/{id} · /config/statustype/{id}. Find a status by id Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: false
expose: false
---
# assets_get_config_statustype_get

`GET /config/statustype/{id}` — /config/statustype/{id}

- Request: [[Assets - GET config statustype {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
