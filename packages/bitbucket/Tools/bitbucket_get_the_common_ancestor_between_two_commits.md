---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_the_common_ancestor_between_two_commits
title: "Bitbucket - Get the common ancestor between two commits"
kind: request
request: "[[Bitbucket - Get the common ancestor between two commits]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/merge-base/{revspec} · Get the common ancestor between two commits. Returns the best common ancestor between two commits, specified in a revspec of 2 commits (e.g. 3a8b42..9ff173). If more than one best common ancestor exists, only one will be returned. It is unspecified which will be returned. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "revspec":
    type: string
    required: true
    description: "Value of revspec in the path."
writes: false
expose: false
---
# bitbucket_get_the_common_ancestor_between_two_commits

`GET /repositories/{workspace}/{repo_slug}/merge-base/{revspec}` — Get the common ancestor between two commits

- Request: [[Bitbucket - Get the common ancestor between two commits]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
