---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branch-restrictions
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_branch_restriction_rule
title: "Bitbucket - Update a branch restriction rule"
kind: request
request: "[[Bitbucket - Update a branch restriction rule]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/branch-restrictions/{id} · Update a branch restriction rule. Updates an existing branch restriction rule. Fields not present in the request body are ignored. See POST for details. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "id":
    type: string
    required: true
    description: "Value of id in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_a_branch_restriction_rule

`PUT /repositories/{workspace}/{repo_slug}/branch-restrictions/{id}` — Update a branch restriction rule

- Request: [[Bitbucket - Update a branch restriction rule]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
