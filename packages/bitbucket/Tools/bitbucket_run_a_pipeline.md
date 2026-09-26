---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/action
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_run_a_pipeline
title: "Bitbucket - Run a pipeline"
kind: request
request: "[[Bitbucket - Run a pipeline]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/pipelines · Run a pipeline. Endpoint to create and initiate a pipeline. There are a number of different options to initiate a pipeline, where the payload of the request will determine which type of pipeline will be instantiated. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "merge_defaults":
    type: string
    required: false
    description: "Whether to merge repository-level defaults into the supplied YAML. Defaults to false."
  "target_branch_to_create":
    type: string
    required: false
    description: "Optional branch name to create from the requested branch or commit target."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_run_a_pipeline

`POST /repositories/{workspace}/{repo_slug}/pipelines` — Run a pipeline

- Request: [[Bitbucket - Run a pipeline]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
