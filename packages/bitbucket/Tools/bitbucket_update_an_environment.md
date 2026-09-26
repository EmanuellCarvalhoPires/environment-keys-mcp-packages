---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/action
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_an_environment
title: "Bitbucket - Update an environment"
kind: request
request: "[[Bitbucket - Update an environment]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes · Update an environment. Update an environment Writes data: yes."
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
# bitbucket_update_an_environment

`POST /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}/changes` — Update an environment

- Request: [[Bitbucket - Update an environment]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
