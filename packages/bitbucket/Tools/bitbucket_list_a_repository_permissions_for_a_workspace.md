---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_a_repository_permissions_for_a_workspace
title: "Bitbucket - List a repository permissions for a workspace"
kind: request
request: "[[Bitbucket - List a repository permissions for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/permissions/repositories/{repo_slug} · List a repository permissions for a workspace. Returns an object for the repository permission of each user in the requested repository. Permissions returned are effective permissions: the highest level of permission the user has. This does not distinguish between direct and indirect (group) privileges. Writes data: no."
params:
  "repo_slug":
    type: string
    required: true
    description: "Value of reposlug in the path."
  "q":
    type: string
    required: false
    description: "Query string to narrow down the response as per filtering and sorting."
  "sort":
    type: string
    required: false
    description: "Name of a response property sort the result by as per filtering and sorting."
writes: false
expose: false
---
# bitbucket_list_a_repository_permissions_for_a_workspace

`GET /workspaces/{workspace}/permissions/repositories/{repo_slug}` — List a repository permissions for a workspace

- Request: [[Bitbucket - List a repository permissions for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
