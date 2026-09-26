---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/repositories
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_repository_permissions_in_a_workspace_for_a_user
title: "Bitbucket - List repository permissions in a workspace for a user"
kind: request
request: "[[Bitbucket - List repository permissions in a workspace for a user]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /user/workspaces/{workspace}/permissions/repositories · List repository permissions in a workspace for a user. Returns an object for each repository the caller has explicit access to in the specified workspace and their effective permission — the highest level of permission the caller has. Writes data: no."
params:
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
# bitbucket_list_repository_permissions_in_a_workspace_for_a_user

`GET /user/workspaces/{workspace}/permissions/repositories` — List repository permissions in a workspace for a user

- Request: [[Bitbucket - List repository permissions in a workspace for a user]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
