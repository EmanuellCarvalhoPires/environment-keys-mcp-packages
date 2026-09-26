---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branching-model
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_the_branching_model_config_for_a_repository
title: "Bitbucket - Update the branching model config for a repository"
kind: request
request: "[[Bitbucket - Update the branching model config for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/branching-model/settings · Update the branching model config for a repository. Update the branching model configuration for a repository. The development branch can be configured to a specific branch or to track the main branch. When set to a specific branch it must currently exist. Only the passed properties will be updated. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: true
expose: false
---
# bitbucket_update_the_branching_model_config_for_a_repository

`PUT /repositories/{workspace}/{repo_slug}/branching-model/settings` — Update the branching model config for a repository

- Request: [[Bitbucket - Update the branching model config for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
