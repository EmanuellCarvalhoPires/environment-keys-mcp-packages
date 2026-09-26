---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_an_environment
title: "Bitbucket - Get an environment"
kind: request
request: "[[Bitbucket - Get an environment]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/environments/{environment_uuid} · Get an environment. Retrieve an environment Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
  "environment_uuid":
    type: string
    required: true
    description: "The environment UUID."
writes: false
expose: false
---
# bitbucket_get_an_environment

`GET /repositories/{workspace}/{repo_slug}/environments/{environment_uuid}` — Get an environment

- Request: [[Bitbucket - Get an environment]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
