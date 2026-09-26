---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/refs
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_branches_and_tags
title: "Bitbucket - List branches and tags"
kind: request
request: "[[Bitbucket - List branches and tags]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/refs · List branches and tags. Returns the branches and tags in the repository. By default, results will be in the order the underlying source control system returns them and identical to the ordering one sees when running \"$ git show-ref\". Note that this follows simple lexical ordering of the ref names. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "q":
    type: string
    required: false
    description: "Query string to narrow down the response as per filtering and sorting."
  "sort":
    type: string
    required: false
    description: "Field by which the results should be sorted as per filtering and sorting. The name field is handled specially for refs in that, if specified as the sort field, it uses a natural sort order instead of…"
writes: false
expose: true
---
# bitbucket_list_branches_and_tags

`GET /repositories/{workspace}/{repo_slug}/refs` — List branches and tags

- Request: [[Bitbucket - List branches and tags]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
