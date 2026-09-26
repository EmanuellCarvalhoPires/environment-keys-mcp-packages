---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_variables_for_an_environment
title: "Bitbucket - List variables for an environment"
kind: request
request: "[[Bitbucket - List variables for an environment]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables · List variables for an environment. Find deployment environment level variables. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "environment_uuid":
    type: string
    required: true
    description: "The environment."
writes: false
expose: false
---
# bitbucket_list_variables_for_an_environment

`GET /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables` — List variables for an environment

- Request: [[Bitbucket - List variables for an environment]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
