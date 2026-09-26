---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_importsource_mapping_progress
title: "Assets - GET importsource {importSourceId} mapping progress {resourceId}"
kind: request
request: "[[Assets - GET importsource {importSourceId} mapping progress {resourceId}]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /importsource/{importSourceId}/mapping/progress/{resourceId} · /importsource/{importSourceId}/mapping/progress/{resourceId}. Get the progress of an asynchronous schema and mapping operation Writes data: no."
params:
  "importSourceId":
    type: string
    required: true
    description: "Value of importSourceId in the path."
  "resourceId":
    type: string
    required: true
    description: "Value of resourceId in the path."
writes: false
expose: false
---
# assets_get_importsource_mapping_progress

`GET /importsource/{importSourceId}/mapping/progress/{resourceId}` — /importsource/{importSourceId}/mapping/progress/{resourceId}

- Request: [[Assets - GET importsource {importSourceId} mapping progress {resourceId}]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
