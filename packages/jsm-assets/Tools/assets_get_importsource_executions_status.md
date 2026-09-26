---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_importsource_executions_status
title: "Assets - GET importsource {importSourceId} executions {importExecutionId} status"
kind: request
request: "[[Assets - GET importsource {importSourceId} executions {importExecutionId} status]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /importsource/{importSourceId}/executions/{importExecutionId}/status · /importsource/{importSourceId}/executions/{importExecutionId}/status. Get the status of the import Writes data: no."
params:
  "importSourceId":
    type: string
    required: true
    description: "Value of importSourceId in the path."
  "importExecutionId":
    type: string
    required: true
    description: "Value of importExecutionId in the path."
writes: false
expose: false
---
# assets_get_importsource_executions_status

`GET /importsource/{importSourceId}/executions/{importExecutionId}/status` — /importsource/{importSourceId}/executions/{importExecutionId}/status

- Request: [[Assets - GET importsource {importSourceId} executions {importExecutionId} status]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
