---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/action
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_stop_a_pipeline
title: "Bitbucket - Stop a pipeline"
kind: request
request: "[[Bitbucket - Stop a pipeline]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/stopPipeline · Stop a pipeline. Signal the stop of a pipeline and all of its steps that not have completed yet. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "pipeline_uuid":
    type: string
    required: true
    description: "The UUID of the pipeline."
writes: true
expose: false
---
# bitbucket_stop_a_pipeline

`POST /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/stopPipeline` — Stop a pipeline

- Request: [[Bitbucket - Stop a pipeline]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
