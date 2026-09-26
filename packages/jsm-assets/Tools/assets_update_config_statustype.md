---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/config
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_update_config_statustype
title: "Assets - PUT config statustype {id}"
kind: request
request: "[[Assets - PUT config statustype {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · PUT /config/statustype/{id} · /config/statustype/{id}. Update an existing status Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# assets_update_config_statustype

`PUT /config/statustype/{id}` — /config/statustype/{id}

- Request: [[Assets - PUT config statustype {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
