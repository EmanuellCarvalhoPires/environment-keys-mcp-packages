---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_variable_for_a_workspace
title: "Bitbucket - Get variable for a workspace"
kind: request
request: "[[Bitbucket - Get variable for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/pipelines-config/variables/{variable_uuid} · Get variable for a workspace. Retrieve a workspace level variable. Writes data: no."
params:
  "variable_uuid":
    type: string
    required: true
    description: "The UUID of the variable to retrieve."
writes: false
expose: false
---
# bitbucket_get_variable_for_a_workspace

`GET /workspaces/{workspace}/pipelines-config/variables/{variable_uuid}` — Get variable for a workspace

- Request: [[Bitbucket - Get variable for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
