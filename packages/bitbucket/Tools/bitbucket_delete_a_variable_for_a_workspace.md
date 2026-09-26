---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_variable_for_a_workspace
title: "Bitbucket - Delete a variable for a workspace"
kind: request
request: "[[Bitbucket - Delete a variable for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /workspaces/{workspace}/pipelines-config/variables/{variable_uuid} · Delete a variable for a workspace. Delete a workspace level variable. Writes data: yes."
params:
  "variable_uuid":
    type: string
    required: true
    description: "The UUID of the variable to delete."
writes: true
expose: false
---
# bitbucket_delete_a_variable_for_a_workspace

`DELETE /workspaces/{workspace}/pipelines-config/variables/{variable_uuid}` — Delete a variable for a workspace

- Request: [[Bitbucket - Delete a variable for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
