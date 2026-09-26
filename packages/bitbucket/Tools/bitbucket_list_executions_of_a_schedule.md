---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_executions_of_a_schedule
title: "Bitbucket - List executions of a schedule"
kind: request
request: "[[Bitbucket - List executions of a schedule]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}/executions · List executions of a schedule. Retrieve the executions of a given schedule. Writes data: no."
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
# bitbucket_list_executions_of_a_schedule

`GET /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}/executions` — List executions of a schedule

- Request: [[Bitbucket - List executions of a schedule]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
