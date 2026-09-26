---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_repository_runner
title: "Bitbucket - Create repository runner"
kind: request
request: "[[Bitbucket - Create repository runner]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/pipelines-config/runners · Create repository runner. Create repository runner. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
writes: true
expose: false
---
# bitbucket_create_repository_runner

`POST /repositories/{workspace}/{repo_slug}/pipelines-config/runners` — Create repository runner

- Request: [[Bitbucket - Create repository runner]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
