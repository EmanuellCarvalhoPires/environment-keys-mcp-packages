---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_repository
title: "Bitbucket - Create a repository"
kind: request
request: "[[Bitbucket - Create a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug} · Create a repository. Creates a new repository. Note: In order to set the project for the newly created repository, pass in either the project key or the project UUID as part of the request body as shown in the examples below: $ curl -X POST -H \"Content-Type: application/json\" -d '{ \"scm\": \"git\", \"pro… Writes data: yes."
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
# bitbucket_create_a_repository

`POST /repositories/{workspace}/{repo_slug}` — Create a repository

- Request: [[Bitbucket - Create a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
