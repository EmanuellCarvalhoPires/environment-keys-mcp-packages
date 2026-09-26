---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_an_environment
title: "Bitbucket - Create an environment"
kind: request
request: "[[Bitbucket - Create an environment]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/environments · Create an environment. Create an environment. Writes data: yes."
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
# bitbucket_create_an_environment

`POST /repositories/{workspace}/{repo_slug}/environments` — Create an environment

- Request: [[Bitbucket - Create an environment]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
