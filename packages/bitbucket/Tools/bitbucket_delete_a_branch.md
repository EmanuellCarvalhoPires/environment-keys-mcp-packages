---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/refs
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_branch
title: "Bitbucket - Delete a branch"
kind: request
request: "[[Bitbucket - Delete a branch]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/refs/branches/{name} · Delete a branch. Delete a branch in the specified repository. The main branch is not allowed to be deleted and will return a 400 response. The branch name should not include any prefixes (e.g. refs/heads). Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "name":
    type: string
    required: true
    description: "Value of name in the path."
writes: true
expose: false
---
# bitbucket_delete_a_branch

`DELETE /repositories/{workspace}/{repo_slug}/refs/branches/{name}` — Delete a branch

- Request: [[Bitbucket - Delete a branch]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
