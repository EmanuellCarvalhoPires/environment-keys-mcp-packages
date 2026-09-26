---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_variable_for_an_environment
title: "Bitbucket - Create a variable for an environment"
kind: request
request: "[[Bitbucket - Create a variable for an environment]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables · Create a variable for an environment. Create a deployment environment level variable. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "environment_uuid":
    type: string
    required: true
    description: "The environment."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_create_a_variable_for_an_environment

`POST /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables` — Create a variable for an environment

- Request: [[Bitbucket - Create a variable for an environment]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
