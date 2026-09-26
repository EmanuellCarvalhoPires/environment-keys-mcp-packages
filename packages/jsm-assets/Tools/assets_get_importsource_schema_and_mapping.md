---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_importsource_schema_and_mapping
title: "Assets - GET importsource {importSourceId} schema-and-mapping"
kind: request
request: "[[Assets - GET importsource {importSourceId} schema-and-mapping]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /importsource/{importSourceId}/schema-and-mapping · /importsource/{importSourceId}/schema-and-mapping. Get the current schema and mapping of the import configuration Writes data: no."
params:
  "importSourceId":
    type: string
    required: true
    description: "Value of importSourceId in the path."
writes: false
expose: false
---
# assets_get_importsource_schema_and_mapping

`GET /importsource/{importSourceId}/schema-and-mapping` — /importsource/{importSourceId}/schema-and-mapping

- Request: [[Assets - GET importsource {importSourceId} schema-and-mapping]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
