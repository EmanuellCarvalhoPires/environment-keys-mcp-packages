---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_importsource_configstatus
title: "Assets - GET importsource {importSourceId} configstatus"
kind: request
request: "[[Assets - GET importsource {importSourceId} configstatus]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /importsource/{importSourceId}/configstatus · /importsource/{importSourceId}/configstatus. Get the current status of the import configuration Writes data: no."
params:
  "importSourceId":
    type: string
    required: true
    description: "Value of importSourceId in the path."
writes: false
expose: false
---
# assets_get_importsource_configstatus

`GET /importsource/{importSourceId}/configstatus` — /importsource/{importSourceId}/configstatus

- Request: [[Assets - GET importsource {importSourceId} configstatus]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
