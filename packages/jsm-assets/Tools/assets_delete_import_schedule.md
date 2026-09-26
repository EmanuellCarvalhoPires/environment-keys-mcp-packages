---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_delete_import_schedule
title: "Assets - Delete import schedule"
kind: request
request: "[[Assets - Delete import schedule]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · DELETE /importsource/{importSourceId}/importschedule/{importScheduleId} · Delete import schedule. Deletes a scheduled import configuration. The import source will remain, but will no longer execute on a schedule. Writes data: yes."
params:
  "importSourceId":
    type: string
    required: true
    description: "The ID of the import source"
  "importScheduleId":
    type: string
    required: true
    description: "The ID of the import schedule to delete"
writes: true
expose: false
---
# assets_delete_import_schedule

`DELETE /importsource/{importSourceId}/importschedule/{importScheduleId}` — Delete import schedule

- Request: [[Assets - Delete import schedule]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
