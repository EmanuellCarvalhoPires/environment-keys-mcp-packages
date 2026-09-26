---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branch-restrictions
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_branch_restriction_rule
title: "Bitbucket - Get a branch restriction rule"
kind: request
request: "[[Bitbucket - Get a branch restriction rule]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/branch-restrictions/{id} · Get a branch restriction rule. Returns a specific branch restriction rule. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: false
expose: false
---
# bitbucket_get_a_branch_restriction_rule

`GET /repositories/{workspace}/{repo_slug}/branch-restrictions/{id}` — Get a branch restriction rule

- Request: [[Bitbucket - Get a branch restriction rule]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
