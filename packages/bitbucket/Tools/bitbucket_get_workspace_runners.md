---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_workspace_runners
title: "Bitbucket - Get workspace runners"
kind: request
request: "[[Bitbucket - Get workspace runners]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/pipelines-config/runners · Get workspace runners. Retrieve workspace runners. Writes data: no."
writes: false
expose: false
---
# bitbucket_get_workspace_runners

`GET /workspaces/{workspace}/pipelines-config/runners` — Get workspace runners

- Request: [[Bitbucket - Get workspace runners]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
