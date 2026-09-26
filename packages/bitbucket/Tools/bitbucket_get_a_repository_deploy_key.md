---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/deployments
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_repository_deploy_key
title: "Bitbucket - Get a repository deploy key"
kind: request
request: "[[Bitbucket - Get a repository deploy key]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id} · Get a repository deploy key. Returns the deploy key belonging to a specific key. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "key_id":
    type: string
    required: true
    description: "Value of keyid in the path."
writes: false
expose: false
---
# bitbucket_get_a_repository_deploy_key

`GET /repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}` — Get a repository deploy key

- Request: [[Bitbucket - Get a repository deploy key]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
