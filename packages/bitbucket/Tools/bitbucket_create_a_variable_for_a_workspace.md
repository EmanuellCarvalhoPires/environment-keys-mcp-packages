---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_variable_for_a_workspace
title: "Bitbucket - Create a variable for a workspace"
kind: request
request: "[[Bitbucket - Create a variable for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /workspaces/{workspace}/pipelines-config/variables · Create a variable for a workspace. Create a workspace level variable. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_create_a_variable_for_a_workspace

`POST /workspaces/{workspace}/pipelines-config/variables` — Create a variable for a workspace

- Request: [[Bitbucket - Create a variable for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
