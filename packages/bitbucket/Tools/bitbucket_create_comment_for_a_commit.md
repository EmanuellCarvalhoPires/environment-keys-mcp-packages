---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/commits
  - api/operation/create
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_create_comment_for_a_commit
title: "Bitbucket - Create comment for a commit"
kind: request
request: "[[Bitbucket - Create comment for a commit]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · POST /repositories/{workspace}/{repo_slug}/commit/{commit}/comments · Create comment for a commit. Creates new comment on the specified commit. To post a reply to an existing comment, include the parent.id field: $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/commit/db9ba1e031d07a02603eae0e559a7adc010257fc/comments/ \\ -X POST -u evzijst \\ -H 'Content-Type:… Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "commit":
    type: string
    required: true
    description: "Value of commit in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_create_comment_for_a_commit

`POST /repositories/{workspace}/{repo_slug}/commit/{commit}/comments` — Create comment for a commit

- Request: [[Bitbucket - Create comment for a commit]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
