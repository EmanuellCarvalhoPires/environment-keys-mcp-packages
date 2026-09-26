---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_schedule
title: "Bitbucket - Delete a schedule"
kind: request
request: "[[Bitbucket - Delete a schedule]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid} · Delete a schedule. Delete a schedule. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "schedule_uuid":
    type: string
    required: true
    description: "The uuid of the schedule."
writes: true
expose: false
---
# bitbucket_delete_a_schedule

`DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}` — Delete a schedule

- Request: [[Bitbucket - Delete a schedule]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
