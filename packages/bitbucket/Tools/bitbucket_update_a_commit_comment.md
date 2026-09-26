---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_commit_comment
title: "Bitbucket - Update a commit comment"
kind: request
request: "[[Bitbucket - Update a commit comment]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id} · Update a commit comment. Used to update the contents of a comment. Only the content of the comment can be updated. Writes data: yes."
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
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_a_commit_comment

`PUT /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}` — Update a commit comment

- Request: [[Bitbucket - Update a commit comment]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
