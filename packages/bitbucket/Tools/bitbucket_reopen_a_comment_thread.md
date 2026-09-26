---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_reopen_a_comment_thread
title: "Bitbucket - Reopen a comment thread"
kind: request
request: "[[Bitbucket - Reopen a comment thread]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}/resolve · Reopen a comment thread. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "pull_request_id":
    type: string
    required: true
    description: "Value of pullrequestid in the path."
  "comment_id":
    type: string
    required: true
    description: "Value of commentid in the path."
writes: true
expose: false
---
# bitbucket_reopen_a_comment_thread

`DELETE /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}/resolve` — Reopen a comment thread

- Request: [[Bitbucket - Reopen a comment thread]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
