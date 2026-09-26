---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_deployments
title: "Bitbucket - List deployments"
kind: request
request: "[[Bitbucket - List deployments]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/deployments · List deployments. Find deployments Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "The repository."
writes: false
expose: false
---
# bitbucket_list_deployments

`GET /repositories/{workspace}/{repo_slug}/deployments` — List deployments

- Request: [[Bitbucket - List deployments]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
