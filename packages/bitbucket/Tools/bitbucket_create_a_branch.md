---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/refs
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_a_branch
title: "Bitbucket - Create a branch"
kind: request
request: "[[Bitbucket - Create a branch]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/refs/branches · Create a branch. Creates a new branch in the specified repository. The payload of the POST should consist of a JSON document that contains the name of the tag and the target hash. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: true
expose: false
---
# bitbucket_create_a_branch

`POST /repositories/{workspace}/{repo_slug}/refs/branches` — Create a branch

- Request: [[Bitbucket - Create a branch]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
