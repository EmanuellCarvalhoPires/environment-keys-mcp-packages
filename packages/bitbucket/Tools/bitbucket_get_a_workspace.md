---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_workspace
title: "Bitbucket - Get a workspace"
kind: request
request: "[[Bitbucket - Get a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace} · Get a workspace. Returns the requested workspace. Writes data: no."
writes: false
expose: false
---
# bitbucket_get_a_workspace

`GET /workspaces/{workspace}` — Get a workspace

- Request: [[Bitbucket - Get a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
