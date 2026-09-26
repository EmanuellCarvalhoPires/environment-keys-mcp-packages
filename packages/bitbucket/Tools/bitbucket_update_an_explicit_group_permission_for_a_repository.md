---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/update
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_update_an_explicit_group_permission_for_a_repository
title: "Bitbucket - Update an explicit group permission for a repository"
kind: request
request: "[[Bitbucket - Update an explicit group permission for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · PUT /repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug} · Update an explicit group permission for a repository. Updates the group permission, or grants a new permission if one does not already exist. Only users with admin permission for the repository may access this resource. The only authentication method supported for this endpoint is via app passwords. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "group_slug":
    type: string
    required: true
    description: "Value of groupslug in the path."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# bitbucket_update_an_explicit_group_permission_for_a_repository

`PUT /repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}` — Update an explicit group permission for a repository

- Request: [[Bitbucket - Update an explicit group permission for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
