---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_repository_runner
title: "Bitbucket - Update repository runner"
kind: request
request: "[[Bitbucket - Update repository runner]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid} · Update repository runner. Update repository runner. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "runner_uuid":
    type: string
    required: true
    description: "The runner uuid."
writes: true
expose: false
---
# bitbucket_update_repository_runner

`PUT /repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid}` — Update repository runner

- Request: [[Bitbucket - Update repository runner]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
