---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_workspace_runner
title: "Bitbucket - Delete workspace runner"
kind: request
request: "[[Bitbucket - Delete workspace runner]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /workspaces/{workspace}/pipelines-config/runners/{runner_uuid} · Delete workspace runner. Delete workspace runner by uuid. Writes data: yes."
params:
  "runner_uuid":
    type: string
    required: true
    description: "The runner uuid."
writes: true
expose: false
---
# bitbucket_delete_workspace_runner

`DELETE /workspaces/{workspace}/pipelines-config/runners/{runner_uuid}` — Delete workspace runner

- Request: [[Bitbucket - Delete workspace runner]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
