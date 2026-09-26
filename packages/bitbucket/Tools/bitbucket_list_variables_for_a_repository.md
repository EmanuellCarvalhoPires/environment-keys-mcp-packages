---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_variables_for_a_repository
title: "Bitbucket - List variables for a repository"
kind: request
request: "[[Bitbucket - List variables for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines_config/variables · List variables for a repository. Find repository level variables. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
writes: false
expose: false
---
# bitbucket_list_variables_for_a_repository

`GET /repositories/{workspace}/{repo_slug}/pipelines_config/variables` — List variables for a repository

- Request: [[Bitbucket - List variables for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
