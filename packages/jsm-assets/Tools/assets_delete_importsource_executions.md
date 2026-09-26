---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_delete_importsource_executions
title: "Assets - DELETE importsource {importSourceId} executions {importExecutionId}"
kind: request
request: "[[Assets - DELETE importsource {importSourceId} executions {importExecutionId}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · DELETE /importsource/{importSourceId}/executions/{importExecutionId} · /importsource/{importSourceId}/executions/{importExecutionId}. Cancel current on-going import Writes data: yes."
params:
  "importSourceId":
    type: string
    required: true
    description: "Value of importSourceId in the path."
  "importExecutionId":
    type: string
    required: true
    description: "Value of importExecutionId in the path."
writes: true
expose: false
---
# assets_delete_importsource_executions

`DELETE /importsource/{importSourceId}/executions/{importExecutionId}` — /importsource/{importSourceId}/executions/{importExecutionId}

- Request: [[Assets - DELETE importsource {importSourceId} executions {importExecutionId}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
