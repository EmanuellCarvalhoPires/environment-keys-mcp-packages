---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_test_case_reasons_output_for_a_given_test_case_in
title: "Bitbucket - Get test case reasons (output) for a given test case in a step of a pipeline"
kind: request
request: "[[Bitbucket - Get test case reasons (output) for a given test case in a step of a pipeline]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases/{test_case_uuid}/test_case_reasons · Get test case reasons (output) for a given test case in a step of a pipeline.. Writes data: no."
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
  "test_case_uuid":
    type: string
    required: true
    description: "The UUID of the test case."
writes: false
expose: false
---
# bitbucket_get_test_case_reasons_output_for_a_given_test_case_in

`GET /repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases/{test_case_uuid}/test_case_reasons` — Get test case reasons (output) for a given test case in a step of a pipeline.

- Request: [[Bitbucket - Get test case reasons (output) for a given test case in a step of a pipeline]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
