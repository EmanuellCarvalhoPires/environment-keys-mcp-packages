---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_default_reviewers
title: "Bitbucket - List default reviewers"
kind: request
request: "[[Bitbucket - List default reviewers]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/default-reviewers · List default reviewers. Returns the repository's default reviewers. These are the users that are automatically added as reviewers on every new pull request that is created. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: false
expose: false
---
# bitbucket_list_default_reviewers

`GET /repositories/{workspace}/{repo_slug}/default-reviewers` — List default reviewers

- Request: [[Bitbucket - List default reviewers]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
