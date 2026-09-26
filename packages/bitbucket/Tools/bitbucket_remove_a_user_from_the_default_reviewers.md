---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/pullrequests
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_remove_a_user_from_the_default_reviewers
title: "Bitbucket - Remove a user from the default reviewers"
kind: request
request: "[[Bitbucket - Remove a user from the default reviewers]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username} · Remove a user from the default reviewers. Removes a default reviewer from the repository. Writes data: yes."
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
# bitbucket_remove_a_user_from_the_default_reviewers

`DELETE /repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}` — Remove a user from the default reviewers

- Request: [[Bitbucket - Remove a user from the default reviewers]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
