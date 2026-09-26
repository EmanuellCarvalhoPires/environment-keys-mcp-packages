---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_update_importsource_executions_progress
title: "Assets - PUT importsource {importSourceId} executions {importExecutionId} progress"
kind: request
request: "[[Assets - PUT importsource {importSourceId} executions {importExecutionId} progress]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · PUT /importsource/{importSourceId}/executions/{importExecutionId}/progress · /importsource/{importSourceId}/executions/{importExecutionId}/progress. Submit progress of ingesting data Writes data: yes."
params:
  "importSourceId":
    type: string
    required: true
    description: "Value of importSourceId in the path."
  "importExecutionId":
    type: string
    required: true
    description: "Value of importExecutionId in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# assets_update_importsource_executions_progress

`PUT /importsource/{importSourceId}/executions/{importExecutionId}/progress` — /importsource/{importSourceId}/executions/{importExecutionId}/progress

- Request: [[Assets - PUT importsource {importSourceId} executions {importExecutionId} progress]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
