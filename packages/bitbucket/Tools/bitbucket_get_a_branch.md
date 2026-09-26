---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/refs
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_branch
title: "Bitbucket - Get a branch"
kind: request
request: "[[Bitbucket - Get a branch]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/refs/branches/{name} · Get a branch. Returns a branch object within the specified repository. This call requires authentication. Private repositories require the caller to authenticate with an account that has appropriate authorization. For Git, the branch name should not include any prefixes (e.g. refs/heads). Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "name":
    type: string
    required: true
    description: "Value of name in the path."
writes: false
expose: false
---
# bitbucket_get_a_branch

`GET /repositories/{workspace}/{repo_slug}/refs/branches/{name}` — Get a branch

- Request: [[Bitbucket - Get a branch]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
