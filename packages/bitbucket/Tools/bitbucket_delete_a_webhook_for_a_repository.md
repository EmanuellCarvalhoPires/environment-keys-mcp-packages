---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_a_webhook_for_a_repository
title: "Bitbucket - Delete a webhook for a repository"
kind: request
request: "[[Bitbucket - Delete a webhook for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/hooks/{uid} · Delete a webhook for a repository. Deletes the specified webhook subscription from the given repository. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "uid":
    type: string
    required: true
    description: "Value of uid in the path."
writes: true
expose: false
---
# bitbucket_delete_a_webhook_for_a_repository

`DELETE /repositories/{workspace}/{repo_slug}/hooks/{uid}` — Delete a webhook for a repository

- Request: [[Bitbucket - Delete a webhook for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
