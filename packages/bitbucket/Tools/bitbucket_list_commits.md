---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_commits
title: "Bitbucket - List commits"
kind: request
request: "[[Bitbucket - List commits]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/commits · List commits. These are the repository's commits. They are paginated and returned in reverse chronological order, similar to the output of git log. Like these tools, the DAG can be filtered. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: false
expose: true
---
# bitbucket_list_commits

`GET /repositories/{workspace}/{repo_slug}/commits` — List commits

- Request: [[Bitbucket - List commits]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
