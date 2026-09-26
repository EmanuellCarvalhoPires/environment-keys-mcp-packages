---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branch-restrictions
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_branch_restriction_rule
title: "Bitbucket - Delete a branch restriction rule"
kind: request
request: "[[Bitbucket - Delete a branch restriction rule]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/branch-restrictions/{id} · Delete a branch restriction rule. Deletes an existing branch restriction rule. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "id":
    type: string
    required: true
    description: "Value of id in the path."
writes: true
expose: false
---
# bitbucket_delete_a_branch_restriction_rule

`DELETE /repositories/{workspace}/{repo_slug}/branch-restrictions/{id}` — Delete a branch restriction rule

- Request: [[Bitbucket - Delete a branch restriction rule]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
