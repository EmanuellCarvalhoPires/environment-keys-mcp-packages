---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_the_logs_for_the_build_container_or_a_service_cont
title: "Bitbucket - Get the logs for the build container or a service container for a given step of a pipeline"
kind: request
request: "[[Bitbucket - Get the logs for the build container or a service container for a given step of a pipeline]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/logs/{log_uuid} · Get the logs for the build container or a service container for a given step of a pipeline.. Retrieve the log file for a build container or service container. This endpoint supports (and encourages!) the use of HTTP Range requests to deal with potentially very large log files. Writes data: no."
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
  "log_uuid":
    type: string
    required: true
    description: "For the main build container specify the step UUID; for a service container specify the service container UUID"
writes: false
expose: false
---
# bitbucket_get_the_logs_for_the_build_container_or_a_service_cont

`GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/logs/{log_uuid}` — Get the logs for the build container or a service container for a given step of a pipeline.

- Request: [[Bitbucket - Get the logs for the build container or a service container for a given step of a pipeline]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
