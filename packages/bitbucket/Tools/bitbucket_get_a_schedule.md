---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_schedule
title: "Bitbucket - Get a schedule"
kind: request
request: "[[Bitbucket - Get a schedule]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid} · Get a schedule. Retrieve a schedule by its UUID. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "schedule_uuid":
    type: string
    required: true
    description: "The uuid of the schedule."
writes: false
expose: false
---
# bitbucket_get_a_schedule

`GET /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}` — Get a schedule

- Request: [[Bitbucket - Get a schedule]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
