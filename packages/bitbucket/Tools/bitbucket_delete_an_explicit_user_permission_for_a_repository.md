---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Bitbucket]]"
tool: bitbucket_delete_an_explicit_user_permission_for_a_repository
title: "Bitbucket - Delete an explicit user permission for a repository"
kind: request
request: "[[Bitbucket - Delete an explicit user permission for a repository]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · DELETE /repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id} · Delete an explicit user permission for a repository. Deletes the repository user permission between the requested repository and user, if one exists. Only users with admin permission for the repository may access this resource. The only authentication method for this endpoint is via app passwords. Writes data: yes."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "selected_user_id":
    type: string
    required: true
    description: "Value of selecteduserid in the path."
writes: true
expose: false
---
# bitbucket_delete_an_explicit_user_permission_for_a_repository

`DELETE /repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}` — Delete an explicit user permission for a repository

- Request: [[Bitbucket - Delete an explicit user permission for a repository]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: **yes**
