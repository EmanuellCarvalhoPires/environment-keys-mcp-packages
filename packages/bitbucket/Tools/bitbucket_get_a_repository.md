---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_repository
title: "Bitbucket - Get a repository"
kind: request
request: "[[Bitbucket - Get a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug} · Get a repository. Returns the object describing this repository. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: false
expose: true
---
# bitbucket_get_a_repository

`GET /repositories/{workspace}/{repo_slug}` — Get a repository

- Request: [[Bitbucket - Get a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
