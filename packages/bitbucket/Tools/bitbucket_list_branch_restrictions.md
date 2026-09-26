---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/branch-restrictions
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_branch_restrictions
title: "Bitbucket - List branch restrictions"
kind: request
request: "[[Bitbucket - List branch restrictions]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/branch-restrictions · List branch restrictions. Returns a paginated list of all branch restrictions on the repository. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "kind":
    type: string
    required: false
    description: "Branch restrictions of this type"
  "pattern":
    type: string
    required: false
    description: "Branch restrictions applied to branches of this pattern"
writes: false
expose: false
---
# bitbucket_list_branch_restrictions

`GET /repositories/{workspace}/{repo_slug}/branch-restrictions` — List branch restrictions

- Request: [[Bitbucket - List branch restrictions]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
