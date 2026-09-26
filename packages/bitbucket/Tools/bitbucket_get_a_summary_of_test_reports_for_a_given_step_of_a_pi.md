---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_summary_of_test_reports_for_a_given_step_of_a_pi
title: "Bitbucket - Get a summary of test reports for a given step of a pipeline"
kind: request
request: "[[Bitbucket - Get a summary of test reports for a given step of a pipeline]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports · Get a summary of test reports for a given step of a pipeline.. Writes data: no."
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
# bitbucket_get_a_summary_of_test_reports_for_a_given_step_of_a_pi

`GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports` — Get a summary of test reports for a given step of a pipeline.

- Request: [[Bitbucket - Get a summary of test reports for a given step of a pipeline]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
