---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branch-restrictions
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_branch_restriction_rule
title: "Bitbucket - Create a branch restriction rule"
kind: request
request: "[[Bitbucket - Create a branch restriction rule]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/branch-restrictions · Create a branch restriction rule. Creates a new branch restriction rule for a repository. kind describes what will be restricted. Writes data: yes."
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
# bitbucket_create_a_branch_restriction_rule

`POST /repositories/{workspace}/{repo_slug}/branch-restrictions` — Create a branch restriction rule

- Request: [[Bitbucket - Create a branch restriction rule]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
