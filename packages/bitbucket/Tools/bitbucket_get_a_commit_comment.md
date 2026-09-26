---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_commit_comment
title: "Bitbucket - Get a commit comment"
kind: request
request: "[[Bitbucket - Get a commit comment]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id} · Get a commit comment. Returns the specified commit comment. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "commit":
    type: string
    required: true
    description: "Value of commit in the path."
  "comment_id":
    type: string
    required: true
    description: "Value of commentid in the path."
writes: false
expose: false
---
# bitbucket_get_a_commit_comment

`GET /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}` — Get a commit comment

- Request: [[Bitbucket - Get a commit comment]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
