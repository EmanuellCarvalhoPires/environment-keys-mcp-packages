---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_steps_for_a_pipeline
title: "Bitbucket - List steps for a pipeline"
kind: request
request: "[[Bitbucket - List steps for a pipeline]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps · List steps for a pipeline. Find steps for the given pipeline. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "pipeline_uuid":
    type: string
    required: true
    description: "The UUID of the pipeline."
writes: false
expose: false
---
# bitbucket_list_steps_for_a_pipeline

`GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps` — List steps for a pipeline

- Request: [[Bitbucket - List steps for a pipeline]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
