---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branching-model
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_the_branching_model_config_for_a_repository
title: "Bitbucket - Get the branching model config for a repository"
kind: request
request: "[[Bitbucket - Get the branching model config for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/branching-model/settings · Get the branching model config for a repository. Return the branching model configuration for a repository. The returned object: 1. Always has a development property for the development branch. 2. Always a production property for the production branch. The production branch can be disabled. 3. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: false
expose: false
---
# bitbucket_get_the_branching_model_config_for_a_repository

`GET /repositories/{workspace}/{repo_slug}/branching-model/settings` — Get the branching model config for a repository

- Request: [[Bitbucket - Get the branching model config for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
