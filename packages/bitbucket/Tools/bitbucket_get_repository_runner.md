---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_repository_runner
title: "Bitbucket - Get repository runner"
kind: request
request: "[[Bitbucket - Get repository runner]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid} · Get repository runner. Retrieve repository runner by uuid. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "runner_uuid":
    type: string
    required: true
    description: "The runner uuid."
writes: false
expose: false
---
# bitbucket_get_repository_runner

`GET /repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid}` — Get repository runner

- Request: [[Bitbucket - Get repository runner]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
