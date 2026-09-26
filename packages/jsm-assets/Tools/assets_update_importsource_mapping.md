---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_update_importsource_mapping
title: "Assets - PUT importsource {importSourceId} mapping"
kind: request
request: "[[Assets - PUT importsource {importSourceId} mapping]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · PUT /importsource/{importSourceId}/mapping · /importsource/{importSourceId}/mapping. Provide object schema and mapping configuration for the external import Writes data: yes."
params:
  "importSourceId":
    type: string
    required: true
    description: "Value of importSourceId in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# assets_update_importsource_mapping

`PUT /importsource/{importSourceId}/mapping` — /importsource/{importSourceId}/mapping

- Request: [[Assets - PUT importsource {importSourceId} mapping]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
