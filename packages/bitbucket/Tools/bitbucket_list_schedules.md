---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_schedules
title: "Bitbucket - List schedules"
kind: request
request: "[[Bitbucket - List schedules]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines_config/schedules · List schedules. Retrieve the configured schedules for the given repository. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
writes: false
expose: false
---
# bitbucket_list_schedules

`GET /repositories/{workspace}/{repo_slug}/pipelines_config/schedules` — List schedules

- Request: [[Bitbucket - List schedules]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
