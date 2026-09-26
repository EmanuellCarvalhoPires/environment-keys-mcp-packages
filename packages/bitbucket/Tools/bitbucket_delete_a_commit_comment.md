---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_commit_comment
title: "Bitbucket - Delete a commit comment"
kind: request
request: "[[Bitbucket - Delete a commit comment]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id} · Delete a commit comment. Deletes the specified commit comment. Note that deleting comments that have visible replies that point to them will not really delete the resource. This is to retain the integrity of the original comment tree. Writes data: yes."
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
writes: true
expose: false
---
# bitbucket_delete_a_commit_comment

`DELETE /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}` — Delete a commit comment

- Request: [[Bitbucket - Delete a commit comment]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
