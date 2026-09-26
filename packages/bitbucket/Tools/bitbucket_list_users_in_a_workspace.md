---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_list_users_in_a_workspace
title: "Bitbucket - List users in a workspace"
kind: request
request: "[[Bitbucket - List users in a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/members · List users in a workspace. Returns all members of the requested workspace. This endpoint additionally supports filtering by email address, if called by a workspace administrator, integration or workspace access token. Writes data: no."
writes: false
expose: false
---
# bitbucket_list_users_in_a_workspace

`GET /workspaces/{workspace}/members` — List users in a workspace

- Request: [[Bitbucket - List users in a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
