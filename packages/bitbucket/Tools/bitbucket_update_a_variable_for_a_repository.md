---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_variable_for_a_repository
title: "Bitbucket - Update a variable for a repository"
kind: request
request: "[[Bitbucket - Update a variable for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid} · Update a variable for a repository. Update a repository level variable. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "variable_uuid":
    type: string
    required: true
    description: "The UUID of the variable to update."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_a_variable_for_a_repository

`PUT /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid}` — Update a variable for a repository

- Request: [[Bitbucket - Update a variable for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
