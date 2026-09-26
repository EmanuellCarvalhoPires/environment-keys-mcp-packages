---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_workspace_runner
title: "Bitbucket - Update workspace runner"
kind: request
request: "[[Bitbucket - Update workspace runner]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /workspaces/{workspace}/pipelines-config/runners/{runner_uuid} · Update workspace runner. Update workspace runner. Writes data: yes."
params:
  "runner_uuid":
    type: string
    required: true
    description: "The runner uuid."
writes: true
expose: false
---
# bitbucket_update_workspace_runner

`PUT /workspaces/{workspace}/pipelines-config/runners/{runner_uuid}` — Update workspace runner

- Request: [[Bitbucket - Update workspace runner]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
