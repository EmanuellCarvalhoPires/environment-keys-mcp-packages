---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_repository_deploy_keys
title: "Bitbucket - List repository deploy keys"
kind: request
request: "[[Bitbucket - List repository deploy keys]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/deploy-keys · List repository deploy keys. Returns all deploy-keys belonging to a repository. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: false
expose: false
---
# bitbucket_list_repository_deploy_keys

`GET /repositories/{workspace}/{repo_slug}/deploy-keys` — List repository deploy keys

- Request: [[Bitbucket - List repository deploy keys]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
