---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branching-model
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_the_effective_or_currently_applied_branching_model
title: "Bitbucket - Get the effective, or currently applied, branching model for a repository"
kind: request
request: "[[Bitbucket - Get the effective, or currently applied, branching model for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/effective-branching-model · Get the effective, or currently applied, branching model for a repository. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: false
expose: false
---
# bitbucket_get_the_effective_or_currently_applied_branching_model

`GET /repositories/{workspace}/{repo_slug}/effective-branching-model` — Get the effective, or currently applied, branching model for a repository

- Request: [[Bitbucket - Get the effective, or currently applied, branching model for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
