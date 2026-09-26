---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_a_comment_on_a_pull_request
title: "Bitbucket - Get a comment on a pull request"
kind: request
request: "[[Bitbucket - Get a comment on a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id} · Get a comment on a pull request. Returns a specific pull request comment. Writes data: no."
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
writes: false
expose: false
---
# bitbucket_get_a_comment_on_a_pull_request

`GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}` — Get a comment on a pull request

- Request: [[Bitbucket - Get a comment on a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
