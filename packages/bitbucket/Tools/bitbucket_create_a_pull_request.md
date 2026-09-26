---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_pull_request
title: "Bitbucket - Create a pull request"
kind: request
request: "[[Bitbucket - Create a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/pullrequests · Create a pull request. Creates a new pull request where the destination repository is this repository and the author is the authenticated user. The minimum required fields to create a pull request are title and source, specified by a branch name. Writes data: yes."
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
# bitbucket_create_a_pull_request

`POST /repositories/{workspace}/{repo_slug}/pullrequests` — Create a pull request

- Request: [[Bitbucket - Create a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
