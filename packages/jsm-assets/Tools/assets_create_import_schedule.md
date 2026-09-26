---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/create
  - api/effect/write
up: "[[MCP - Assets]]"
tool: assets_create_import_schedule
title: "Assets - Create import schedule"
kind: request
request: "[[Assets - Create import schedule]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Assets · POST /importsource/{importSourceId}/importschedule · Create import schedule. Creates a new scheduled import configuration for the specified import source. Scheduled imports allow you to automate data imports on a recurring basis (daily, weekly, monthly) or run them once at a specific time. Writes data: yes."
params:
  "importSourceId":
    type: string
    required: true
    description: "The ID of the import source to schedule"
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# assets_create_import_schedule

`POST /importsource/{importSourceId}/importschedule` — Create import schedule

- Request: [[Assets - Create import schedule]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
