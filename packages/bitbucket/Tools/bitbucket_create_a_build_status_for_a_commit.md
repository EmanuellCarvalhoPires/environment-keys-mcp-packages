---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commit-statuses
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_build_status_for_a_commit
title: "Bitbucket - Create a build status for a commit"
kind: request
request: "[[Bitbucket - Create a build status for a commit]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build · Create a build status for a commit. Creates a new build status against the specified commit. If the specified key already exists, the existing status object will be overwritten. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "commit":
    type: string
    required: true
    description: "Value of commit in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_create_a_build_status_for_a_commit

`POST /repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build` — Create a build status for a commit

- Request: [[Bitbucket - Create a build status for a commit]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
