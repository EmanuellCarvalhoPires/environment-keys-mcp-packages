---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pipelines
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_variable_for_a_repository
title: "Bitbucket - Delete a variable for a repository"
kind: request
request: "[[Bitbucket - Delete a variable for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid} · Delete a variable for a repository. Delete a repository level variable. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "variable_uuid":
    type: string
    required: true
    description: "The UUID of the variable to delete."
writes: true
expose: false
---
# bitbucket_delete_a_variable_for_a_repository

`DELETE /repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid}` — Delete a variable for a repository

- Request: [[Bitbucket - Delete a variable for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
