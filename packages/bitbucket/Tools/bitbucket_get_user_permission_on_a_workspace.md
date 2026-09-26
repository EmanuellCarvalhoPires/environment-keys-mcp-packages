---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/list
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_user_permission_on_a_workspace
title: "Bitbucket - Get user permission on a workspace"
kind: request
request: "[[Bitbucket - Get user permission on a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /user/workspaces/{workspace}/permission · Get user permission on a workspace. Returns the caller's effective role; as in, the highest level of privilege the caller has for the workspace. If the calling user is a member of multiple groups with distinct roles, only the highest level is returned. Writes data: no."
writes: false
expose: false
---
# bitbucket_get_user_permission_on_a_workspace

`GET /user/workspaces/{workspace}/permission` — Get user permission on a workspace

- Request: [[Bitbucket - Get user permission on a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
