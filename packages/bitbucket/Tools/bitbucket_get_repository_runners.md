---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_repository_runners
title: "Bitbucket - Get repository runners"
kind: request
request: "[[Bitbucket - Get repository runners]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines-config/runners · Get repository runners. Retrieve repository runners. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
writes: false
expose: false
---
# bitbucket_get_repository_runners

`GET /repositories/{workspace}/{repo_slug}/pipelines-config/runners` — Get repository runners

- Request: [[Bitbucket - Get repository runners]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
