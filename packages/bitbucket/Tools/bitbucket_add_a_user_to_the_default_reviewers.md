---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_add_a_user_to_the_default_reviewers
title: "Bitbucket - Add a user to the default reviewers"
kind: request
request: "[[Bitbucket - Add a user to the default reviewers]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username} · Add a user to the default reviewers. Adds the specified user to the repository's list of default reviewers. This method is idempotent. Adding a user a second time has no effect. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "target_username":
    type: string
    required: true
    description: "Value of targetusername in the path."
writes: true
expose: false
---
# bitbucket_add_a_user_to_the_default_reviewers

`PUT /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}` — Add a user to the default reviewers

- Request: [[Bitbucket - Add a user to the default reviewers]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
