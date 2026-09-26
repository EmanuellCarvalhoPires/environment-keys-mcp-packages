---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_schedule
title: "Bitbucket - Update a schedule"
kind: request
request: "[[Bitbucket - Update a schedule]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid} · Update a schedule. Update a schedule. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "schedule_uuid":
    type: string
    required: true
    description: "The uuid of the schedule."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_a_schedule

`PUT /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}` — Update a schedule

- Request: [[Bitbucket - Update a schedule]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
