---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/action
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_approve_a_commit
title: "Bitbucket - Approve a commit"
kind: request
request: "[[Bitbucket - Approve a commit]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/commit/{commit}/approve · Approve a commit. Approve the specified commit as the authenticated user. This operation is only available to users that have explicit access to the repository. In contrast, just the fact that a repository is publicly accessible to users does not give them the ability to approve commits. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "commit":
    type: string
    required: true
    description: "Value of commit in the path."
writes: true
expose: false
---
# bitbucket_approve_a_commit

`POST /repositories/{workspace}/{repo_slug}/commit/{commit}/approve` — Approve a commit

- Request: [[Bitbucket - Approve a commit]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
