---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_user_permissions_in_a_workspace
title: "Bitbucket - List user permissions in a workspace"
kind: request
request: "[[Bitbucket - List user permissions in a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/permissions · List user permissions in a workspace. Returns the list of members in a workspace and their permission levels. Permission can be: owner collaborator member The collaborator role is being removed from the Bitbucket Cloud API. For more information, see the deprecation announcement. Writes data: no."
params:
  "q":
    type: string
    required: false
    description: "Query string to narrow down the response as per filtering and sorting."
writes: false
expose: false
---
# bitbucket_list_user_permissions_in_a_workspace

`GET /workspaces/{workspace}/permissions` — List user permissions in a workspace

- Request: [[Bitbucket - List user permissions in a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
