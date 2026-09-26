---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_commit
title: "Bitbucket - Get a commit"
kind: request
request: "[[Bitbucket - Get a commit]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/commit/{commit} · Get a commit. Returns the specified commit. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "commit":
    type: string
    required: true
    description: "Value of commit in the path."
writes: false
expose: false
---
# bitbucket_get_a_commit

`GET /repositories/{workspace}/{repo_slug}/commit/{commit}` — Get a commit

- Request: [[Bitbucket - Get a commit]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
