---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_log_file_for_a_step
title: "Bitbucket - Get log file for a step"
kind: request
request: "[[Bitbucket - Get log file for a step]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/log · Get log file for a step. Retrieve the log file for a given step of a pipeline. This endpoint supports (and encourages!) the use of HTTP Range requests to deal with potentially very large log files. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "pipeline_uuid":
    type: string
    required: true
    description: "The UUID of the pipeline."
  "step_uuid":
    type: string
    required: true
    description: "The UUID of the step."
writes: false
expose: false
---
# bitbucket_get_log_file_for_a_step

`GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/log` — Get log file for a step

- Request: [[Bitbucket - Get log file for a step]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
