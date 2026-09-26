---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_repository
title: "Bitbucket - Delete a repository"
kind: request
request: "[[Bitbucket - Delete a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug} · Delete a repository. Deletes the repository. This is an irreversible operation. This does not affect its forks. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "redirect_to":
    type: string
    required: false
    description: "If a repository has been moved to a new location, use this parameter to show users a friendly message in the Bitbucket UI that the repository has moved to a new location."
writes: true
expose: false
---
# bitbucket_delete_a_repository

`DELETE /repositories/{workspace}/{repo_slug}` — Delete a repository

- Request: [[Bitbucket - Delete a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
