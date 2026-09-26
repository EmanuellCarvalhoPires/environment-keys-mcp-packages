---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_variable_for_a_repository
title: "Bitbucket - Get a variable for a repository"
kind: request
request: "[[Bitbucket - Get a variable for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid} · Get a variable for a repository. Retrieve a repository level variable. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "variable_uuid":
    type: string
    required: true
    description: "The UUID of the variable to retrieve."
writes: false
expose: false
---
# bitbucket_get_a_variable_for_a_repository

`GET /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid}` — Get a variable for a repository

- Request: [[Bitbucket - Get a variable for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
