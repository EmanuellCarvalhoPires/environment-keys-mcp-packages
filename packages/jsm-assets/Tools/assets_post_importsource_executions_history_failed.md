---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_post_importsource_executions_history_failed
title: "Assets - POST importsource {importSourceId} executions {executionId} history failed"
kind: request
request: "[[Assets - POST importsource {importSourceId} executions {executionId} history failed]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /importsource/{importSourceId}/executions/{executionId}/history/failed · /importsource/{importSourceId}/executions/{executionId}/history/failed. Creates a failed import history record for the specified import source and execution with the given failure reason Writes data: yes."
params:
  "importSourceId":
    type: string
    required: true
    description: "Value of importSourceId in the path."
  "executionId":
    type: string
    required: true
    description: "Value of executionId in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# assets_post_importsource_executions_history_failed

`POST /importsource/{importSourceId}/executions/{executionId}/history/failed` — /importsource/{importSourceId}/executions/{executionId}/history/failed

- Request: [[Assets - POST importsource {importSourceId} executions {executionId} history failed]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
