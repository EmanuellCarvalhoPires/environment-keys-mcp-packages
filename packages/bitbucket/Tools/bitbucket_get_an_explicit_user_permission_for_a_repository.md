---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_an_explicit_user_permission_for_a_repository
title: "Bitbucket - Get an explicit user permission for a repository"
kind: request
request: "[[Bitbucket - Get an explicit user permission for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id} · Get an explicit user permission for a repository. Returns the explicit user permission for a given user and repository. Only users with admin permission for the repository may access this resource. Permissions can be: admin write read none Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "selected_user_id":
    type: string
    required: true
    description: "Value of selecteduserid in the path."
writes: false
expose: false
---
# bitbucket_get_an_explicit_user_permission_for_a_repository

`GET /repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}` — Get an explicit user permission for a repository

- Request: [[Bitbucket - Get an explicit user permission for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
