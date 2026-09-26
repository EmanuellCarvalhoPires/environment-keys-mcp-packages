---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_variable_for_a_workspace
title: "Bitbucket - Update variable for a workspace"
kind: request
request: "[[Bitbucket - Update variable for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /workspaces/{workspace}/pipelines-config/variables/{variable_uuid} · Update variable for a workspace. Update a workspace level variable. Writes data: yes."
params:
  "variable_uuid":
    type: string
    required: true
    description: "The UUID of the variable."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_variable_for_a_workspace

`PUT /workspaces/{workspace}/pipelines-config/variables/{variable_uuid}` — Update variable for a workspace

- Request: [[Bitbucket - Update variable for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
