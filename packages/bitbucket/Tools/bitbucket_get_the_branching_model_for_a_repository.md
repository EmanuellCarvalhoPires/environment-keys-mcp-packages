---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branching-model
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_the_branching_model_for_a_repository
title: "Bitbucket - Get the branching model for a repository"
kind: request
request: "[[Bitbucket - Get the branching model for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/branching-model · Get the branching model for a repository. Return the branching model as applied to the repository. This view is read-only. The branching model settings can be changed using the settings API. The returned object: 1. Always has a development property. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: false
expose: false
---
# bitbucket_get_the_branching_model_for_a_repository

`GET /repositories/{workspace}/{repo_slug}/branching-model` — Get the branching model for a repository

- Request: [[Bitbucket - Get the branching model for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
