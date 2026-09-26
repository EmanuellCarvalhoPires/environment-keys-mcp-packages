---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_importsource_executions_status_get
title: "Assets - GET importsource {importSourceId} executions status"
kind: request
request: "[[Assets - GET importsource {importSourceId} executions status]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /importsource/{importSourceId}/executions/status · /importsource/{importSourceId}/executions/status. Get the status of the most recently created import execution Writes data: no."
params:
  "importSourceId":
    type: string
    required: true
    description: "Value of importSourceId in the path."
writes: false
expose: false
---
# assets_get_importsource_executions_status_get

`GET /importsource/{importSourceId}/executions/status` — /importsource/{importSourceId}/executions/status

- Request: [[Assets - GET importsource {importSourceId} executions status]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
