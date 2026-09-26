---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commit-statuses
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_build_status_for_a_commit
title: "Bitbucket - Get a build status for a commit"
kind: request
request: "[[Bitbucket - Get a build status for a commit]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key} · Get a build status for a commit. Returns the specified build status for a commit. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "commit":
    type: string
    required: true
    description: "Value of commit in the path."
  "key":
    type: string
    required: true
    description: "Value of key in the path."
writes: false
expose: false
---
# bitbucket_get_a_build_status_for_a_commit

`GET /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key}` — Get a build status for a commit

- Request: [[Bitbucket - Get a build status for a commit]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
