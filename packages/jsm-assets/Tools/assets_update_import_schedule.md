---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_update_import_schedule
title: "Assets - Update import schedule"
kind: request
request: "[[Assets - Update import schedule]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · PUT /importsource/{importSourceId}/importschedule/{importScheduleId} · Update import schedule. Updates an existing scheduled import configuration. You can modify the start time, run interval, or callback URL. Writes data: yes."
params:
  "importSourceId":
    type: string
    required: true
    description: "The ID of the import source"
  "importScheduleId":
    type: string
    required: true
    description: "The ID of the import schedule to update"
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# assets_update_import_schedule

`PUT /importsource/{importSourceId}/importschedule/{importScheduleId}` — Update import schedule

- Request: [[Assets - Update import schedule]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
