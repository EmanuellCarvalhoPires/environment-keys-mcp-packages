---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_explicit_group_permissions_for_a_repository
title: "Bitbucket - List explicit group permissions for a repository"
kind: request
request: "[[Bitbucket - List explicit group permissions for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/permissions-config/groups · List explicit group permissions for a repository. Returns a paginated list of explicit group permissions for the given repository. This endpoint does not support BBQL features. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
writes: false
expose: false
---
# bitbucket_list_explicit_group_permissions_for_a_repository

`GET /repositories/{workspace}/{repo_slug}/permissions-config/groups` — List explicit group permissions for a repository

- Request: [[Bitbucket - List explicit group permissions for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
