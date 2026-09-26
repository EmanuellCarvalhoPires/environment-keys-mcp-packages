---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/config
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_delete_config_statustype
title: "Assets - DELETE config statustype {id}"
kind: request
request: "[[Assets - DELETE config statustype {id}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · DELETE /config/statustype/{id} · /config/statustype/{id}. Delete an existing status Writes data: yes."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: true
expose: false
---
# assets_delete_config_statustype

`DELETE /config/statustype/{id}` — /config/statustype/{id}

- Request: [[Assets - DELETE config statustype {id}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
