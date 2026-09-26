---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_add_a_repository_deploy_key
title: "Bitbucket - Add a repository deploy key"
kind: request
request: "[[Bitbucket - Add a repository deploy key]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/deploy-keys · Add a repository deploy key. Create a new deploy key in a repository. Note: If authenticating a deploy key with an OAuth consumer, any changes to the OAuth consumer will subsequently invalidate the deploy key. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: true
expose: false
---
# bitbucket_add_a_repository_deploy_key

`POST /repositories/{workspace}/{repo_slug}/deploy-keys` — Add a repository deploy key

- Request: [[Bitbucket - Add a repository deploy key]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
