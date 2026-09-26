---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_workspace_runner
title: "Bitbucket - Create workspace runner"
kind: request
request: "[[Bitbucket - Create workspace runner]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /workspaces/{workspace}/pipelines-config/runners · Create workspace runner. Create workspace runner. Writes data: yes."
writes: true
expose: false
---
# bitbucket_create_workspace_runner

`POST /workspaces/{workspace}/pipelines-config/runners` — Create workspace runner

- Request: [[Bitbucket - Create workspace runner]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
