---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_import_source_by_id
title: "Assets - Get import source by ID"
kind: request
request: "[[Assets - Get import source by ID]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /importsource/{id} · Get import source by ID. Retrieves a specific import source configuration by its ID. If scheduled imports are enabled, the response includes scheduling information. Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: false
expose: false
---
# assets_get_import_source_by_id

`GET /importsource/{id}` — Get import source by ID

- Request: [[Assets - Get import source by ID]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
