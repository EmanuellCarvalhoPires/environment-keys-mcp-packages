---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_repositories_watchers
title: "Bitbucket - List repositories watchers"
kind: request
request: "[[Bitbucket - List repositories watchers]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/watchers · List repositories watchers. Returns a paginated list of all the watchers on the specified repository. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: false
expose: false
---
# bitbucket_list_repositories_watchers

`GET /repositories/{workspace}/{repo_slug}/watchers` — List repositories watchers

- Request: [[Bitbucket - List repositories watchers]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
