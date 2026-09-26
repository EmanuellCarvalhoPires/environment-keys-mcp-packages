---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_schedule
title: "Bitbucket - Create a schedule"
kind: request
request: "[[Bitbucket - Create a schedule]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/pipelines_config/schedules · Create a schedule. Create a schedule for the given repository. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_create_a_schedule

`POST /repositories/{workspace}/{repo_slug}/pipelines_config/schedules` — Create a schedule

- Request: [[Bitbucket - Create a schedule]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
