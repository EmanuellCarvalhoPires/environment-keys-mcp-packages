---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_an_environment
title: "Bitbucket - Delete an environment"
kind: request
request: "[[Bitbucket - Delete an environment]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/environments/{environment_uuid} · Delete an environment. Delete an environment Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "environment_uuid":
    type: string
    required: true
    description: "The environment UUID."
writes: true
expose: false
---
# bitbucket_delete_an_environment

`DELETE /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}` — Delete an environment

- Request: [[Bitbucket - Delete an environment]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
