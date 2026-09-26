---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_repository_forks
title: "Bitbucket - List repository forks"
kind: request
request: "[[Bitbucket - List repository forks]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/forks · List repository forks. Returns a paginated list of all the forks of the specified repository. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
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
expose: false
---
# bitbucket_list_repository_forks

`GET /repositories/{workspace}/{repo_slug}/forks` — List repository forks

- Request: [[Bitbucket - List repository forks]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
