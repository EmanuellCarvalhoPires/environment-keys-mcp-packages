---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/action
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_post_importsource_executions_data
title: "Assets - POST importsource {importSourceId} executions {importExecutionId} data"
kind: request
request: "[[Assets - POST importsource {importSourceId} executions {importExecutionId} data]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /importsource/{importSourceId}/executions/{importExecutionId}/data · /importsource/{importSourceId}/executions/{importExecutionId}/data. Providing data to be ingested Writes data: yes."
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
# assets_post_importsource_executions_data

`POST /importsource/{importSourceId}/executions/{importExecutionId}/data` — /importsource/{importSourceId}/executions/{importExecutionId}/data

- Request: [[Assets - POST importsource {importSourceId} executions {importExecutionId} data]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
