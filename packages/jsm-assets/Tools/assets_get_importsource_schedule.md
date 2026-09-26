---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/list
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_importsource_schedule
title: "Assets - GET importsource {importSourceId} schedule"
kind: request
request: "[[Assets - GET importsource {importSourceId} schedule]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /importsource/{importSourceId}/schedule · /importsource/{importSourceId}/schedule. Retrieve links for import schedule operations (create, get, update, delete). Returns a createSchedule link to POST a new schedule, and if a schedule already exists, returns a schedule link that can be used with GET, PUT, or DELETE operations. Writes data: no."
params:
  "importSourceId":
    type: string
    required: true
    description: "Value of importSourceId in the path."
writes: false
expose: false
---
# assets_get_importsource_schedule

`GET /importsource/{importSourceId}/schedule` — /importsource/{importSourceId}/schedule

- Request: [[Assets - GET importsource {importSourceId} schedule]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
