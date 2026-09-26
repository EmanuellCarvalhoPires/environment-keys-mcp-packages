---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_environments
title: "Bitbucket - List environments"
kind: request
request: "[[Bitbucket - List environments]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/environments · List environments. Find environments Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
writes: false
expose: false
---
# bitbucket_list_environments

`GET /repositories/{workspace}/{repo_slug}/environments` — List environments

- Request: [[Bitbucket - List environments]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
