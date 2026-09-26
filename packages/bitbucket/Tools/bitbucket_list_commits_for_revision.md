---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_commits_for_revision
title: "Bitbucket - List commits for revision"
kind: request
request: "[[Bitbucket - List commits for revision]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/commits/{revision} · List commits for revision. These are the repository's commits. They are paginated and returned in reverse chronological order, similar to the output of git log. Like these tools, the DAG can be filtered. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "revision":
    type: string
    required: true
    description: "Value of revision in the path."
writes: false
expose: false
---
# bitbucket_list_commits_for_revision

`GET /repositories/{workspace}/{repo_slug}/commits/{revision}` — List commits for revision

- Request: [[Bitbucket - List commits for revision]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
