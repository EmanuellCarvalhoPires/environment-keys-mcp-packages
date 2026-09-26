---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/action
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_fork_a_repository
title: "Bitbucket - Fork a repository"
kind: request
request: "[[Bitbucket - Fork a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/forks · Fork a repository. Creates a new fork of the specified repository. Forking a repository To create a fork, specify the workspace explicitly as part of the request body: $ curl -X POST -u jdoe https://api.bitbucket.org/2.0/repositories/atlassian/bbql/forks \\ -H 'Content-Type: application/json' -d '{… Writes data: yes."
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
# bitbucket_fork_a_repository

`POST /repositories/{workspace}/{repo_slug}/forks` — Fork a repository

- Request: [[Bitbucket - Fork a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
