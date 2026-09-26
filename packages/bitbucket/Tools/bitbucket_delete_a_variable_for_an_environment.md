---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_variable_for_an_environment
title: "Bitbucket - Delete a variable for an environment"
kind: request
request: "[[Bitbucket - Delete a variable for an environment]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid} · Delete a variable for an environment. Delete a deployment environment level variable. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "environment_uuid":
    type: string
    required: true
    description: "The environment."
  "variable_uuid":
    type: string
    required: true
    description: "The UUID of the variable to delete."
writes: true
expose: false
---
# bitbucket_delete_a_variable_for_an_environment

`DELETE /repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables/{variable_uuid}` — Delete a variable for an environment

- Request: [[Bitbucket - Delete a variable for an environment]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
