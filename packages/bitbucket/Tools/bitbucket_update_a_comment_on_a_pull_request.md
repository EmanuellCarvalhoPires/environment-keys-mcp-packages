---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_a_comment_on_a_pull_request
title: "Bitbucket - Update a comment on a pull request"
kind: request
request: "[[Bitbucket - Update a comment on a pull request]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id} · Update a comment on a pull request. Updates a specific pull request comment. Writes data: yes."
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
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_a_comment_on_a_pull_request

`PUT /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}` — Update a comment on a pull request

- Request: [[Bitbucket - Update a comment on a pull request]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
