---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_default_reviewer_get
title: "Bitbucket - Get a default reviewer (GET)"
kind: request
request: "[[Bitbucket - Get a default reviewer (GET)]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username} · Get a default reviewer. Returns the specified reviewer. This can be used to test whether a user is among the repository's default reviewers list. A 404 indicates that that specified user is not a default reviewer. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "target_username":
    type: string
    required: true
    description: "Value of targetusername in the path."
writes: false
expose: false
---
# bitbucket_get_a_default_reviewer_get

`GET /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}` — Get a default reviewer

- Request: [[Bitbucket - Get a default reviewer (GET)]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
