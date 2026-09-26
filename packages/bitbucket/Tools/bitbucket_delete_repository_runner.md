---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_repository_runner
title: "Bitbucket - Delete repository runner"
kind: request
request: "[[Bitbucket - Delete repository runner]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid} · Delete repository runner. Delete repository runner by uuid. Writes data: yes."
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
# bitbucket_delete_repository_runner

`DELETE /repositories/{workspace}/{repo_slug}/pipelines-config/runners/{runner_uuid}` — Delete repository runner

- Request: [[Bitbucket - Delete repository runner]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
