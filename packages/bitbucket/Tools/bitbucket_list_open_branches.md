---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/refs
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_open_branches
title: "Bitbucket - List open branches"
kind: request
request: "[[Bitbucket - List open branches]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/refs/branches · List open branches. Returns a list of all open branches within the specified repository. Results will be in the order the source control manager returns them. Branches support filtering and sorting that can be used to search for specific branches. Writes data: no."
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
    description: "Field by which the results should be sorted as per filtering and sorting. The name field is handled specially for branches in that, if specified as the sort field, it uses a natural sort order instead…"
writes: false
expose: false
---
# bitbucket_list_open_branches

`GET /repositories/{workspace}/{repo_slug}/refs/branches` — List open branches

- Request: [[Bitbucket - List open branches]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
