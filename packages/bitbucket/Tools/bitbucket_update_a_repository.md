---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_repository
title: "Bitbucket - Update a repository"
kind: request
request: "[[Bitbucket - Update a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug} · Update a repository. Since this endpoint can be used to both update and to create a repository, the request body depends on the intent. Creation See the POST documentation for the repository endpoint for an example of the request body. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_a_repository

`PUT /repositories/{workspace}/{repo_slug}` — Update a repository

- Request: [[Bitbucket - Update a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
