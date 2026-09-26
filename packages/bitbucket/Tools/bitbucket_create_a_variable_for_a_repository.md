---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_variable_for_a_repository
title: "Bitbucket - Create a variable for a repository"
kind: request
request: "[[Bitbucket - Create a variable for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/pipelines_config/variables · Create a variable for a repository. Create a repository level variable. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_create_a_variable_for_a_repository

`POST /repositories/{workspace}/{repo_slug}/pipelines_config/variables` — Create a variable for a repository

- Request: [[Bitbucket - Create a variable for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
