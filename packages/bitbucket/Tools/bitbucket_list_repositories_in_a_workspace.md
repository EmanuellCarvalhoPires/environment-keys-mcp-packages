---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_repositories_in_a_workspace
title: "Bitbucket - List repositories in a workspace"
kind: request
request: "[[Bitbucket - List repositories in a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace} · List repositories in a workspace. Returns a paginated list of all repositories owned by the specified workspace. The result can be narrowed down based on the authenticated user's role. E.g. Writes data: no."
params:
  "role":
    type: string
    required: false
    description: "Filters the result based on the authenticated user's role on each repository. member: returns repositories to which the user has explicit read access contributor: returns repositories to which the use…"
  "q":
    type: string
    required: false
    description: "Query string to narrow down the response as per filtering and sorting."
  "sort":
    type: string
    required: false
    description: "Field by which the results should be sorted as per filtering and sorting."
writes: false
expose: true
---
# bitbucket_list_repositories_in_a_workspace

`GET /repositories/{workspace}` — List repositories in a workspace

- Request: [[Bitbucket - List repositories in a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
