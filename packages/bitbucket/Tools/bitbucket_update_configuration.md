---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_configuration
title: "Bitbucket - Update configuration"
kind: request
request: "[[Bitbucket - Update configuration]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/pipelines_config · Update configuration. Update the pipelines configuration for a repository. Writes data: yes."
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
# bitbucket_update_configuration

`PUT /repositories/{workspace}/{repo_slug}/pipelines_config` — Update configuration

- Request: [[Bitbucket - Update configuration]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
