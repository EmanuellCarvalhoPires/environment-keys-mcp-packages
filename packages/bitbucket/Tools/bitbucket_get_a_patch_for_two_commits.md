---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_patch_for_two_commits
title: "Bitbucket - Get a patch for two commits"
kind: request
request: "[[Bitbucket - Get a patch for two commits]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/patch/{spec} · Get a patch for two commits. Produces a raw patch for a single commit (diffed against its first parent), or a patch-series for a revspec of 2 commits (e.g. 3a8b42..9ff173 where the first commit represents the source and the second commit the destination). Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "spec":
    type: string
    required: true
    description: "Value of spec in the path."
writes: false
expose: false
---
# bitbucket_get_a_patch_for_two_commits

`GET /repositories/{workspace}/{repo_slug}/patch/{spec}` — Get a patch for two commits

- Request: [[Bitbucket - Get a patch for two commits]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
