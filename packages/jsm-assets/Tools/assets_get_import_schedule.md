---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/get
  - api/effect/read
up: "[[MCP - Assets]]"
tool: assets_get_import_schedule
title: "Assets - Get import schedule"
kind: request
request: "[[Assets - Get import schedule]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · GET /importsource/{importSourceId}/importschedule/{importScheduleId} · Get import schedule. Retrieves a specific scheduled import configuration by ID Writes data: no."
params:
  "importSourceId":
    type: string
    required: true
    description: "The ID of the import source"
  "importScheduleId":
    type: string
    required: true
    description: "The ID of the import schedule"
writes: false
expose: false
---
# assets_get_import_schedule

`GET /importsource/{importSourceId}/importschedule/{importScheduleId}` — Get import schedule

- Request: [[Assets - Get import schedule]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
