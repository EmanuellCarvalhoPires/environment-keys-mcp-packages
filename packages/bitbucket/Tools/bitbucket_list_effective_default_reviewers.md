---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_effective_default_reviewers
title: "Bitbucket - List effective default reviewers"
kind: request
request: "[[Bitbucket - List effective default reviewers]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/effective-default-reviewers · List effective default reviewers. Returns the repository's effective default reviewers. This includes both default reviewers defined at the repository level as well as those inherited from its project. These are the users that are automatically added as reviewers on every new pull request that is created. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: false
expose: false
---
# bitbucket_list_effective_default_reviewers

`GET /repositories/{workspace}/{repo_slug}/effective-default-reviewers` — List effective default reviewers

- Request: [[Bitbucket - List effective default reviewers]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
