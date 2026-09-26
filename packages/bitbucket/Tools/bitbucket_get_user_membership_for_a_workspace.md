---
tags:
  - mcp/tool
  - api/service/bitbucket
  - api/app/bitbucket
  - api/resource/workspaces
  - api/operation/get
  - api/effect/read
up: "[[MCP - Bitbucket]]"
tool: bitbucket_get_user_membership_for_a_workspace
title: "Bitbucket - Get user membership for a workspace"
kind: request
request: "[[Bitbucket - Get user membership for a workspace]]"
service_tag: bitbucket/workspace
service_param: instance
service_exclude_tag: template
description: "Bitbucket · GET /workspaces/{workspace}/members/{member} · Get user membership for a workspace. Returns the workspace membership, which includes a User object for the member and a Workspace object for the requested workspace. Writes data: no."
params:
  "member":
    type: string
    required: true
    description: "Value of member in the path."
writes: false
expose: false
---
# bitbucket_get_user_membership_for_a_workspace

`GET /workspaces/{workspace}/members/{member}` — Get user membership for a workspace

- Request: [[Bitbucket - Get user membership for a workspace]]
- Instance: `instance` parameter (notes tagged `bitbucket/workspace`)
- Writes data: no
