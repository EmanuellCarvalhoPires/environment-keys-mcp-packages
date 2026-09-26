---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_workspace_runner
title: "Bitbucket - Get workspace runner"
kind: request
request: "[[Bitbucket - Get workspace runner]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/pipelines-config/runners/{runner_uuid} · Get workspace runner. Get workspace runner by uuid. Writes data: no."
params:
  "runner_uuid":
    type: string
    required: true
    description: "The runner uuid."
writes: false
expose: false
---
# bitbucket_get_workspace_runner

`GET /workspaces/{workspace}/pipelines-config/runners/{runner_uuid}` — Get workspace runner

- Request: [[Bitbucket - Get workspace runner]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
