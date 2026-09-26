---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_post_importsource_executions
title: "Assets - POST importsource {importSourceId} executions"
kind: request
request: "[[Assets - POST importsource {importSourceId} executions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /importsource/{importSourceId}/executions · /importsource/{importSourceId}/executions. Move to the data ingestion steps of external imports Writes data: yes."
params:
  "importSourceId":
    type: string
    required: true
    description: "Value of importSourceId in the path."
writes: true
expose: false
---
# assets_post_importsource_executions

`POST /importsource/{importSourceId}/executions` — /importsource/{importSourceId}/executions

- Request: [[Assets - POST importsource {importSourceId} executions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
