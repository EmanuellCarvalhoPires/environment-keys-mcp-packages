---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_variables_for_a_workspace
title: "Bitbucket - List variables for a workspace"
kind: request
request: "[[Bitbucket - List variables for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/pipelines-config/variables · List variables for a workspace. Find workspace level variables. Writes data: no."
writes: false
expose: false
---
# bitbucket_list_variables_for_a_workspace

`GET /workspaces/{workspace}/pipelines-config/variables` — List variables for a workspace

- Request: [[Bitbucket - List variables for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
