---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_configuration
title: "Bitbucket - Get configuration"
kind: request
request: "[[Bitbucket - Get configuration]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines_config · Get configuration. Retrieve the repository pipelines configuration. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
writes: false
expose: false
---
# bitbucket_get_configuration

`GET /repositories/{workspace}/{repo_slug}/pipelines_config` — Get configuration

- Request: [[Bitbucket - Get configuration]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
